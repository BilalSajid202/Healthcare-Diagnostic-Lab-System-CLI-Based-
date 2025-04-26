from config.config import get_db_connection

class ReportController:

    def generate_patient_report(self, patient_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            query = """
                SELECT p.name, t.test_name, r.value AS result, b.bill_amount AS amount, tr.test_date AS date
                FROM Patients p
                JOIN TestRequests tr ON p.id = tr.patient_id
                JOIN Tests t ON tr.test_id = t.id
                LEFT JOIN Results r ON tr.id = r.request_id
                LEFT JOIN Billing b ON p.id = b.patient_id
                WHERE p.id = %s
            """
            cursor.execute(query, (patient_id,))
            rows = cursor.fetchall()

            if rows:
                print(f"\n📝 Report for Patient ID: {patient_id}")
                for row in rows:
                    print(f"🔬 Test: {row[1]}, 🧾 Result: {row[2]}, 💵 Bill: {row[3]}, 📅 Date: {row[4]}")
            else:
                print("❌ No records found for this patient.")
        except Exception as e:
            print(f"❌ Error generating report: {e}")
        finally:
            cursor.close()
            conn.close()
