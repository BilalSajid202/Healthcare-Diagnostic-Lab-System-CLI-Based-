from config.config import get_db_connection

class PatientModel:
    @staticmethod
    def insert_patient(patient):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO Patients (name, dob, contact) VALUES (%s, %s, %s)
        """
        cursor.execute(query, patient)
        conn.commit()
        cursor.close()
        conn.close()