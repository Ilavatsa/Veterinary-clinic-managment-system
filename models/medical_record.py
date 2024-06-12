from db_helper import execute_query, fetch

class MedicalRecord:
    def create_table(self):
        """Create the medical_record table."""
        query = """
        CREATE TABLE IF NOT EXISTS medical_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_id INTEGER,
            visit_date TIMESTAMP,
            diagnosis TEXT,
            treatment_plan TEXT,
            FOREIGN KEY (pet_id) REFERENCES pet(id)
        );
        """
        execute_query(query)

    def create(self, pet_id, visit_date, diagnosis, treatment_plan):
        """Create a new medical record."""
        query = f"""
        INSERT INTO medical_record (pet_id, visit_date, diagnosis, treatment_plan)
        VALUES ({pet_id}, '{visit_date}', '{diagnosis}', '{treatment_plan}');
        """
        execute_query(query)

    def drop_table(self):
        """Drop the medical_record table."""
        query = "DROP TABLE IF EXISTS medical_record;"
        execute_query(query)


