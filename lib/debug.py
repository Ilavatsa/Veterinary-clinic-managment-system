import sqlite3

def create_tables():
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    # Create the owner table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS owner (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT,
            phone_number TEXT
        )
    ''')

    # Create the pet table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            species TEXT,
            age INTEGER,
            owner_id INTEGER,
            vet_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owner (id),
            FOREIGN KEY (vet_id) REFERENCES veterinarian (id)
        )
    ''')

    # Create the veterinarian table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS veterinarian (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            specialty TEXT,
            phone_number TEXT
        )
    ''')

    # Create the appointment table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointment (
            id INTEGER PRIMARY KEY,
            date TEXT,
            time TEXT,
            pet_id INTEGER,
            vet_id INTEGER,
            FOREIGN KEY (pet_id) REFERENCES pet (id),
            FOREIGN KEY (vet_id) REFERENCES veterinarian (id)
        )
    ''')

    # Create the treatment table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS treatment (
            id INTEGER PRIMARY KEY,
            description TEXT,
            cost REAL,
            appointment_id INTEGER,
            FOREIGN KEY (appointment_id) REFERENCES appointment (id)
        )
    ''')

    # Create the medical_record table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medical_record (
            id INTEGER PRIMARY KEY,
            record_date TEXT,
            details TEXT,
            pet_id INTEGER,
            FOREIGN KEY (pet_id) REFERENCES pet (id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()


