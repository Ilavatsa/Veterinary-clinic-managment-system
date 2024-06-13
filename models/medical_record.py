import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_helper import execute_query, fetch

class MedicalRecord:
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS medical_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_id INTEGER,
            record_date TIMESTAMP NOT NULL,
            details TEXT,
            FOREIGN KEY (pet_id) REFERENCES pet(id)
        );
        '''
        execute_query(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS medical_record;"
        execute_query(query)

    def create(self, pet_id, record_date, details):
        query = '''
        INSERT INTO medical_record (pet_id, record_date, details) 
        VALUES (?, ?, ?, ?);
        '''
        execute_query(query, (pet_id, record_date, details))

    def all(self):
        query = "SELECT * FROM medical_record;"
        return fetch(query)

    def find_by_id(self, record_id):
        query = "SELECT * FROM medical_record WHERE id = ?;"
        return fetch(query, (record_id,))
