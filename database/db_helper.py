
import sqlite3

def connect():
    """Connect to the SQLite database."""
    return sqlite3.connect('veterinary_clinic.db')

def execute_query(query):
    """Execute a query on the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

def fetch(query):
    """Fetch data from the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data
