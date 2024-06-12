from db_helper import execute_query, fetch

class Pet:
    def create_table(self):
        """Create the pet table."""
        query = """
        CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            species TEXT,
            breed TEXT,
            age INTEGER,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owner(id)
        );
        """
        execute_query(query)

    def create(self, name, species, breed, age, owner_id):
        """Create a new pet."""
        query = f"""
        INSERT INTO pet (name, species, breed, age, owner_id)
        VALUES ('{name}', '{species}', '{breed}', {age}, {owner_id});
        """
        execute_query(query)

    def drop_table(self):
        """Drop the pet table."""
        query = "DROP TABLE IF EXISTS pet;"
        execute_query(query)

