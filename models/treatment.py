from debug import cursor

class Treatment:
    def __init__(self, description, cost, appointment_id, id=None):
        self.id = id
        self.description = description
        self.cost = cost
        self.appointment_id = appointment_id

    def save(self):
        sql = """
            INSERT INTO treatments (description
            ++
            
            
            , cost, appointment_id) VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.description, self.cost, self.appointment_id))
        cursor.connection.commit()
        self.id = cursor.lastrowid

    def delete(self):
        sql = """
            DELETE FROM treatments WHERE id = ?
        """
        cursor.execute(sql, (self.id,))
        cursor.connection.commit()
