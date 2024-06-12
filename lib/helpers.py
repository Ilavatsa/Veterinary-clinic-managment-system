import sqlite3

DATABASE_NAME = 'vet_clinic.db'

def connect():
    return sqlite3.connect(DATABASE_NAME)

def execute_query(query, params=()):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor

def fetch_all(query, params=()):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

def fetch_one(query, params=()):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
