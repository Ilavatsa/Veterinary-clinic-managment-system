# debug.py

import sqlite3

# Establish the connection to the SQLite database
conn = sqlite3.connect('vet_clinic.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Function to initialize the database tables if they do not exist
def initialize_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS owners (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT,
        phone_number TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        species TEXT,
        breed TEXT,
        age INTEGER,
        owner_id INTEGER,
        FOREIGN KEY (owner_id) REFERENCES owners (id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS veterinarians (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialty TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        reason TEXT,
        pet_id INTEGER,
        veterinarian_id INTEGER,
        FOREIGN KEY (pet_id) REFERENCES pets (id),
        FOREIGN KEY (veterinarian_id) REFERENCES veterinarians (id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treatments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        cost REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medical_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        record_date TEXT NOT NULL,
        details TEXT,
        pet_id INTEGER,
        FOREIGN KEY (pet_id) REFERENCES pets (id)
    )
    """)

    conn.commit()

# Call the function to initialize the database tables
initialize_db()
