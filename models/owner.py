import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_helper import execute_query, fetch

class Owner:
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS owner (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        );
        '''
        execute_query(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS owner;"
        execute_query(query)

    def create(self, name, email, phone):
        query = '''
        INSERT INTO owner (name, email, phone) 
        VALUES (?, ?, ?);
        '''
        execute_query(query, (name, email, phone))

    def all(self):
        query = "SELECT * FROM owner;"
        return fetch(query)

    def find_by_id(self, owner_id):
        query = "SELECT * FROM owner WHERE id = ?;"
        return fetch(query, (owner_id,))

