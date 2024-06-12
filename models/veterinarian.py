from db_helper import execute_query, fetch

class Veterinarian:
    def create_table(self):
        """Create the veterinarian table."""
        query = """
        CREATE TABLE IF NOT EXISTS veterinarian (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            specialization TEXT,
            phone_number TEXT
        );
        """
        execute_query(query)

    def create(self, name, specialization, phone_number):
        """Create a new veterinarian."""
        query = f"""
        INSERT INTO veterinarian (name, specialization, phone_number)
        VALUES ('{name}', '{specialization}', '{phone_number}');
        """
        execute_query(query)

    def drop_table(self):
        """Drop the veterinarian table."""
        query = "DROP TABLE IF EXISTS veterinarian;"
        execute_query(query)
