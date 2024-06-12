from debug import cursor

class Pet:
    def __init__(self, name, species, age, owner_id, vet_id, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.owner_id = owner_id
        self.vet_id = vet_id

    def save(self):
        sql = """
            INSERT INTO pets (name, species, age, owner_id, vet-id) VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.species, self.age, self.owner_id, self.vet_id))
        cursor.connection.commit()
        self.id = cursor.lastrowid

    def delete(self):
        sql = """
            DELETE FROM pets WHERE id = ?
        """
        cursor.execute(sql, (self.id,))
        cursor.connection.commit()
