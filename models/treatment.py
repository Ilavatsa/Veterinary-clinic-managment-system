import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_helper import execute_query, fetch

class Treatment:
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS treatment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_id INTEGER,
            veterinarian_id INTEGER,
            treatment_date TIMESTAMP NOT NULL,
            description TEXT NOT NULL,
            FOREIGN KEY (pet_id) REFERENCES pet(id),
            FOREIGN KEY (veterinarian_id) REFERENCES veterinarian(id)
        );
        '''
        execute_query(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS treatment;"
        execute_query(query)

    def create(self, pet_id, veterinarian_id, treatment_date, description):
        query = '''
        INSERT INTO treatment (pet_id, veterinarian_id, treatment_date, description) 
        VALUES (?, ?, ?, ?);
        '''
        execute_query(query, (pet_id, veterinarian_id, treatment_date, description))

    def all(self):
        query = "SELECT * FROM treatment;"
        return fetch(query)

    def find_by_id(self, treatment_id):
        query = "SELECT * FROM treatment WHERE id = ?;"
        return fetch(query, (treatment_id,))
