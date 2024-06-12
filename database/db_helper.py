import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("vet_clinic.db")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    database = "vet_clinic.db"
    conn = create_connection()

    if conn is not None:
        with open("database/create_tables.sql", "r") as sql_file:
            sql_script = sql_file.read()
        for sql in sql_script.split(";"):
            if sql.strip():
                create_table(conn, sql)
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()
