import sqlite3

def create_tables():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    # Define the SQL commands to create the tables
    create_owner_table = """
        CREATE TABLE IF NOT EXISTS owner (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT,
            phone_number TEXT
        )
    """

    # Define similar SQL commands for other tables: Pet, Veterinarian, Appointment, Treatment, MedicalRecord

    # Execute the SQL commands to create the tables
    cursor.execute(create_owner_table)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()

