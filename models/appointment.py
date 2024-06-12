from debug import cursor

class Appointment:
    def __init__(self, date, time, pet_id, vet_id, id=None):
        self.id = id
        self.date = date
        self.time = time
        self.pet_id = pet_id
        self.vet_id = vet_id

    def save(self):
        sql = """
            INSERT INTO appointments (date, time, pet_id, vet_id) VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.date, self.time, self.pet_id, self.vet_id))
        cursor.connection.commit()
        self.id = cursor.lastrowid

    def delete(self):
        sql = """
            DELETE FROM appointments WHERE id = ?
        """
        cursor.execute(sql, (self.id,))
        cursor.connection.commit()