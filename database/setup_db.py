from db_helper import execute_query

def setup_database():
    """Setup the database by creating tables."""
    with open('create_tables.sql', 'r') as f:
        sql_script = f.read()
        execute_query(sql_script)

if __name__ == "__main__":
    setup_database()

