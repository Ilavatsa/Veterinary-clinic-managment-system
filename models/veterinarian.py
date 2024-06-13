import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_helper import execute_query, fetch

class Veterinarian:
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS veterinarian (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialty TEXT NOT NULL,
            phone TEXT NOT NULL
        );
        '''
        execute_query(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS veterinarian;"
        execute_query(query)

    def create(self, name, specialty, phone):
        query = '''
        INSERT INTO veterinarian (name, specialty, phone) 
        VALUES (?, ?, ?);
        '''
        execute_query(query, (name, specialty, phone))

    def all(self):
        query = "SELECT * FROM veterinarian;"
        return fetch(query)

    def find_by_id(self, veterinarian_id):
        query = "SELECT * FROM veterinarian WHERE id = ?;"
        return fetch(query, (veterinarian_id,))
