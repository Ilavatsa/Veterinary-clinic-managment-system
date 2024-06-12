from debug import cursor

class Veterinanrian:
    def __init__(self, name, specialty, phone_number, id=None):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.phone_number = phone_number

    def save(self):
        sql = """
            INSERT INTO veterinarians (name, specialty, phone_number) VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.specialty, self.phone_number))
        cursor.connection.commit()
        self.id = cursor.lastrowid

    def delete(self):
        sql = """
            DELETE FROM veterinarians WHERE id = ?
        """
        cursor.execute(sql, (self.id,))
        cursor.connection.commit()
