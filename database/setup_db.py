import sqlite3

def setup_database():
    with open('database/create_tables.sql', 'r') as f:
        sql = f.read()
    
    conn = sqlite3.connect('veterinary_clinic.db')
    cursor = conn.cursor()
    cursor.executescript(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()


