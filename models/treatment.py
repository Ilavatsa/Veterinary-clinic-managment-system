from db_helper import execute_query, fetch

class Treatment:
    def create_table(self):
        """Create the treatment table."""
        query = """
        CREATE TABLE IF NOT EXISTS treatment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_id INTEGER,
            appointment_id INTEGER,
            treatment_date TIMESTAMP,
            description TEXT,
            FOREIGN KEY (pet_id) REFERENCES pet(id),
            FOREIGN KEY (appointment_id) REFERENCES appointment(id)
        );
        """
        execute_query(query)

    def create(self, pet_id, appointment_id, treatment_date, description):
        """Create a new treatment."""
        query = f"""
        INSERT INTO treatment (pet_id, appointment_id, treatment_date, description)
        VALUES ({pet_id}, {appointment_id}, '{treatment_date}', '{description}');
        """
        execute_query(query)

    def drop_table(self):
        """Drop the treatment table."""
        query = "DROP TABLE IF EXISTS treatment;"
        execute_query(query)
