# 🐍 Program: SQLite3 Database Connection, Table Creation, Data Insertion & Fetching
# -------------------------------------------------------------------------------
# Demonstrates:
# 1. Database connection
# 2. Table creation
# 3. Data insertion
# 4. Fetching and displaying records

import sqlite3

connection = None  # ✅ Initialize here to avoid 'unbound' error

try:
    # Step 1: Connect to database (creates file if it doesn't exist)
    connection = sqlite3.connect("student_data.db")
    cursor = connection.cursor()
    print("✅ Connected to SQLite3 database successfully!")

    # Step 2: Create a table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    """)
    print("📘 Table 'students' created successfully!")

    # Step 3: Insert sample data
    students_data = [
        ("Alice", 20, "A"),
        ("Bob", 22, "B"),
        ("Charlie", 19, "A+")
    ]
    cursor.executemany(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students_data)
    print("📝 Sample data inserted successfully!")

    # Step 4: Fetch and display all records
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n🎯 Student Records in Database:")
    print("-" * 40)
    for row in records:
        print(
            f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Grade: {row[3]}")
    print("-" * 40)

except sqlite3.Error as e:
    print(f"❌ SQLite3 Error: {e}")

finally:
    # Step 5: Close connection safely
    if connection:
        connection.commit()
        connection.close()
        print("🔒 Database connection closed successfully.")
