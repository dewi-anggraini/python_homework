import sqlite3
import csv

# Task 1: Create & connect a New SQLite Database
try:
   # connect to the magazines database
   conn = sqlite3.connect("../db/magazines.db")
   conn.execute("PRAGMA foreign_keys = 1") # enforce foreign keys
   cur = conn.cursor()
   print("Database created & connected successfully")


# Task 2: Define Database Structure
   # Drop existing tables (for fresh start)
   cur.execute("DROP TABLE IF EXISTS subscriptions")
   cur.execute("DROP TABLE IF EXISTS subscribers")
   cur.execute("DROP TABLE IF EXISTS magazines")
   cur.execute("DROP TABLE IF EXISTS publishers")

   # Create Tables
   cur.execute("""
               CREATE TABLE publishers (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT UNIQUE NOT NULL
               )
   """)

   cur.execute("""
   CREATE TABLE magazines (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT UNIQUE NOT NULL,
               publisher_id INTEGER NOT NULL,
               FOREIGN KEY(publisher_id) REFERENCES publishers(id)
   )
   """)

   cur.execute("""
   CREATE TABLE subscribers (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT NOT NULL,
               address TEXT NOT NULL,
              UNIQUE (name, address)
   )
   """)

   cur.execute("""
   CREATE TABLE subscriptions (
               subscriber_id INTEGER NOT NULL,
               magazine_id INTEGER NOT NULL,
               expiration_date TEXT NOT NULL, 
               PRIMARY KEY(subscriber_id, magazine_id),
               FOREIGN KEY(subscriber_id) REFERENCES subscribers(id),
               FOREIGN KEY(magazine_id) REFERENCES magazines(id)
   )
   """)

   conn.commit()
   
# Verify tables 
   cur.execute("SELECT name FROM sqlite_master WHERE type='table';") 
   tables = cur.fetchall() 
   print("Tables in database:", tables)
   print("Tables created successfully")

# Task 3: Populate Tables with Data
# Using functions to add entries
   def add_publisher(conn, name):
      try:
         cur = conn.cursor()
         cur.execute("SELECT id FROM publishers WHERE name = ?", (name,))
         if cur.fetchone():
            print(f"Publisher '{name}' already exist.")
            return
         cur.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
         print(f"Publisher '{name}' added.")
      except sqlite3.Error as e:
         print(f"Error adding publisher: {e}")

   def add_magazine(conn, name, publisher_id):
      try:
         cur = conn.cursor()
         cur.execute("SELECT id FROM magazines WHERE name = ?", (name,))
         if cur.fetchone():
            print(f"Magazine '{name}' already exist.")
            return
         cur.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
         print(f"Magazine '{name}' added.")
      except sqlite3.Error as e:
         print(f"Error adding magazine: {e}")

   def add_subscriber(conn, name, address):
      try:
         cur = conn.cursor()
         cur.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
         if cur.fetchone():
            print(f"Subscriber '{name}, {address}' already exist.")
            return
         cur.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
         print(f"Subscriber '{name}, {address}' added.")
      except sqlite3.Error as e:
         print(f"Error adding subscriber: {e}")

   def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
      try:
         cur = conn.cursor()
         cur.execute("SELECT 1 FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
         if cur.fetchone():
            print(f"Subscription already exist for subscriber {subscriber_id} and magazine '{magazine_id}.")
            return
         cur.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))
         print(f"Subscription added: subscriber {subscriber_id}, magazine {magazine_id}, expiration {expiration_date}.")
      except sqlite3.Error as e:
         print(f"Error adding subscription: {e}")

   # Populate tables with each 3 entries
   if __name__ == "__main__":
      # Publishers
      add_publisher(conn, "National Geographic Partners")
      add_publisher(conn, "Forbes Media")
      add_publisher(conn, "Well+Good LLC")

      # Magazines
      add_magazine(conn, "National Geographic", 1)
      add_magazine(conn, "Forbes", 2)
      add_magazine(conn, "Well+Good", 3)

      # Subscribers
      add_subscriber(conn, "Harry Potter", "123 Grinderwald St")
      add_subscriber(conn, "Tom Riddle", "456 Slytherin St")
      add_subscriber(conn, "Alice Wonderland", "789 Wonder St")

      # Subscriptions
      add_subscription(conn, 1, 1, "2026-12-01")
      add_subscription(conn, 2, 2, "2026-11-01")
      add_subscription(conn, 3, 3, "2026-10-01")

   conn.commit()
   print("All entries committed successfully.")

   # Task 4: Write SQL Queries
   # Subscribers
   print("\nAll Subscribers:")
   cur.execute("SELECT*FROM subscribers;")
   for row in cur.fetchall():
      print(row)

   # Magazines
   print("\nAll Magazines sorted by Names:")
   cur.execute("SELECT*FROM magazines ORDER by name;")
   for row in cur.fetchall():
      print(row)

   # Magazine by Publisher
   publisher_name = "National Geographic Partners"
   print(f"\nMagazines Published by {publisher_name}:")
   cur.execute("""
               SELECT magazines.id, magazines.name, publishers.name as publisher_name 
               FROM magazines 
               JOIN publishers ON magazines.publisher_id = publishers.id
               WHERE publishers.name = ?;
   """, (publisher_name,))
   for row in cur.fetchall():
      print(row)

except Exception as e:
   print(f"SQLite error: {e}")

# Connection closed
finally: 
   if conn: 
      conn.close() 
      print("Connection closed.")




