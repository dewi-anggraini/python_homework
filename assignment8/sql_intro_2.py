import sqlite3
import pandas as pd


# Task 5: Read Data into a DataFrame
try:
    # Step 1: Connect to the database
    conn = sqlite3.connect("../db/lesson.db ")
    cursor = conn.cursor()

    # List all tables in the database 
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") 
    tables = cursor.fetchall() 
    print("Tables in lesson.db:", tables)
    
    # Step 2: Read data into DataFrame using SQL JOIN (using aliases)
    query = """
    SELECT 
        li.line_item_id,
        li.quantity,
        li.product_id,
        p.product_name,
        p.price
    FROM line_items li
    JOIN products p ON li.product_id = p.product_id    
    """
    df = pd.read_sql_query(query, conn)

    # Step 3: Print first 5 rows
    print("Initial DataFrame")
    print(df.head())

    # Step 4: Add "total" column (quabtity*price)
    df['total'] = df['quantity'] * df['price']
    print("\nDataFrame with 'total' column")
    print(df.head())

    # Step 5: Group by product_id
    summary = df.groupby('product_id').agg({
        'line_item_id': 'count',  # for how many times ordered
        'total': 'sum',           # for total price
        'product_name': 'first'   # for product names
    }).reset_index()

    # Step 6: Print first 5 rows for summary
    print("\nGrouped summary DataFrame:")
    print(summary.head())

    # Step 7: Sort by product_name
    summary = summary.sort_values(by='product_name')
    print("\nSorted Summary DataFrame:")
    print(summary.head())

    # Step 8: Write to csv in assignment8 directory
    summary.to_csv("../assignment8/order_summary.csv", index=False)
    print("\nCSV file to assignment8 Directory")

except Exception as e:
    print("Error:", e)

# close connection
finally:
    if 'conn' in locals():
        conn.close()   
