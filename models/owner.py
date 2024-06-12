from debug import cursor

class Owner:
    def __init__(self, name, address, phone_number, id=None):
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def save(self):
        sql = """
            INSERT INTO owner (name, address, phone_number) VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.address, self.phone_number))
        cursor.connection.commit()
        self.id = cursor.lastrowid

    def delete(self):
        sql = """
            DELETE FROM owners WHERE id = ?
        """
        cursor.execute(sql, (self.id,))
        cursor.connection.commit()
