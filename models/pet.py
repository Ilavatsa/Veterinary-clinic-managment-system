import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_helper import execute_query, fetch

class Pet:
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            breed TEXT NOT NULL,
            age INTEGER NOT NULL,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owner(id)
        );
        '''
        execute_query(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS pet;"
        execute_query(query)

    def create(self, name, species, breed, age, owner_id):
        query = '''
        INSERT INTO pet (name, species, breed, age, owner_id) 
        VALUES (?, ?, ?, ?, ?);
        '''
        execute_query(query, (name, species, breed, age, owner_id))

    def all(self):
        query = "SELECT * FROM pet;"
        return fetch(query)

    def find_by_id(self, pet_id):
        query = "SELECT * FROM pet WHERE id = ?;"
        return fetch(query, (pet_id,))
