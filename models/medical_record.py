from debug import cursor

class MedicalRecord:
    def __init__(self, record_date, details, pet_id, id=None):
        self.id = id
        self.record_date = record_date
        self.details = details
        self.pet_id = pet_id

    def save(self):
        sql = """
            INSERT INTO medical_records (record_date, details, pet_id) VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.record_date, self.details, self.pet_id))
        cursor.connection.commit()
        self.id = cursor.lastrowid

    def delete(self):
        sql = """
            DELETE FROM medical_records WHERE id = ?
        """
        cursor.execute(sql, (self.id,))
        cursor.connection.commit()
