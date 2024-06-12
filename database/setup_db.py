import sqlite3

def setup_database():
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    with open('database/create_tables.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
