from db_helper import execute_query, fetch

class Appointment:
    def create_table(self):
        """Create the appointment table."""
        query = """
        CREATE TABLE IF NOT EXISTS appointment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_id INTEGER,
            appointment_date TIMESTAMP,
            status TEXT,
            description TEXT,
            FOREIGN KEY (pet_id) REFERENCES pet(id)
        );
        """
        execute_query(query)

    def create(self, pet_id, appointment_date, status, description):
        """Create a new appointment."""
        query = f"""
        INSERT INTO appointment (pet_id, appointment_date, status, description)
        VALUES ({pet_id}, '{appointment_date}', '{status}', '{description}');
        """
        execute_query(query)

    def drop_table(self):
        """Drop the appointment table."""
        query = "DROP TABLE IF EXISTS appointment;"
        execute_query(query)
