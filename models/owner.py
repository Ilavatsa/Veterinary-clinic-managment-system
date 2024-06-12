from db_helper import execute_query, fetch

class Owner:
    def create_table(self):
        """Create the owner table."""
        query = """
        CREATE TABLE IF NOT EXISTS owner (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone_number TEXT
        );
        """
        execute_query(query)

    def create(self, name, email, phone_number):
        """Create a new owner."""
        query = f"""
        INSERT INTO owner (name, email, phone_number)
        VALUES ('{name}', '{email}', '{phone_number}');
        """
        execute_query(query)

    def drop_table(self):
        """Drop the owner table."""
        query = "DROP TABLE IF EXISTS owner;"
        execute_query(query)

