import sqlite3

def execute_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

# Task 1: Complex JOINs with Aggregation
def total_price(conn):
    print("\nTotal Price of first5 orders:")
    query = """
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
    """
    for row in execute_query(conn, query):
        print(row)

# Task 2: Understanding Subqueries
def average_price(conn):
    print("\nAverage Price of orders per customer:")
    query = """
    SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
    FROM customers c
    LEFT JOIN (
         SELECT o.order_id, o.customer_id, SUM(p.price * li.quantity) AS total_price
         FROM orders o
         JOIN line_items li ON o.order_id = li.order_id
         JOIN products p ON li.product_id = p.product_id
         GROUP BY o.order_id
    ) sub
    ON c.customer_id = sub.customer_id
    GROUP BY c.customer_id;
    """
    for row in execute_query(conn, query):
        print(row)

# Task 3: An Insert Transaction Based on existing Data
def new_transaction(conn):
    print("\nNew Transaction Based on Data:")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Get customer id
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = ?", ("Perez and Sons",))
    customer_id = cursor.fetchone()[0]

    # Get employee_id
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?", ("Miranda", "Harris"))
    employee_id = cursor.fetchone()[0]

    # Get 5 least expensive product_ids
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    # Insert order and line items with try-except
    try:
        # Start transaction
        cursor.execute(
            "INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id",
            (customer_id, employee_id)
        )
        order_id = cursor.fetchone()[0]

        # Insert line items
        for product_id in product_ids:
            cursor.execute(
            "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
            (order_id, product_id, 10)
            )

        conn.commit()

        # Print line items
        cursor.execute(""" 
                    SELECT li.line_item_id, li.quantity, p.product_name
                    FROM line_items li
                    JOIN products p ON li.product_id = p.product_id
                    WHERE li.order_id =?;                   
                    """, (order_id,))
        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        conn.rollback()
        print("\nInsert Failed:", e)

# Task 4: Aggregation with HAVING
def employees_order(conn):
    print("\nEmployees with more than 5 orders:")
    query = """
    SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    GROUP BY e.employee_id
    HAVING COUNT(o.order_id) > 5;
    """
    for row in execute_query(conn, query):
        print(row)

def main():
    conn = sqlite3.connect("../db/lesson.db")

    total_price(conn)
    average_price(conn)
    new_transaction(conn)
    employees_order(conn)

    conn.close()

if __name__ == "__main__":
    main()


    






    

    