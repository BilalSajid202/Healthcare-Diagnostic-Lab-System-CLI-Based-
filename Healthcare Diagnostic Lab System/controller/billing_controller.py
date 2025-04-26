from model.billing_model import BillingModel
from config.config import get_db_connection
import csv
from datetime import datetime
import os

class BillingController:
    def generate_bill(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            patient_id = input("🔹 Enter Patient ID: ").strip()

            # Fetch patient details
            cursor.execute("SELECT name, contact FROM Patients WHERE id = %s", (patient_id,))
            patient = cursor.fetchone()

            if not patient:
                print("❌ Patient not found.")
                return

            patient_name, patient_contact = patient
            print(f"👤 Patient: {patient_name}, 📞 Contact: {patient_contact}")

            # Optional: process billing (will invoke stored procedure)
            BillingModel.process_billing(int(patient_id))

            # Fetch test details for the patient
            cursor.execute("""
                SELECT t.id, t.test_name, r.value AS test_result, 50 AS cost
                FROM Tests t
                JOIN TestRequests tr ON t.id = tr.test_id
                JOIN Results r ON tr.id = r.request_id
                WHERE tr.patient_id = %s
            """, (patient_id,))
            tests = cursor.fetchall()

            if not tests:
                print("❌ No test records found for billing.")
                return

            total_amount = 0
            bill_data = []

            for test_id, test_name, test_result, test_cost in tests:
                total_amount += test_cost
                bill_data.append([
                    patient_id, patient_name, test_id, test_name, test_result, f"{test_cost:.2f}"
                ])

            # Add total row
            bill_data.append([
                patient_id, patient_name, '', 'TOTAL', '', f"{total_amount:.2f}"
            ])

            # Save to CSV
            self.save_bill_to_csv(bill_data, patient_id)

            print("✅ Bill successfully generated and saved!")

        except Exception as e:
            print(f"❌ Error during bill generation: {e}")
        finally:
            cursor.close()
            conn.close()

    def save_bill_to_csv(self, bill_data, patient_id):
        # Create a unique filename per patient per day
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bill_patient_{patient_id}_{timestamp}.csv"
        filepath = os.path.join("bills", filename)

        # Ensure 'bills' directory exists
        os.makedirs("bills", exist_ok=True)

        try:
            with open(filepath, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'Patient ID', 'Patient Name', 'Test ID', 
                    'Test Name', 'Test Result', 'Cost'
                ])
                writer.writerows(bill_data)
            print(f"🧾 Bill saved at: {filepath}")
        except Exception as e:
            print(f"❌ Failed to save bill CSV: {e}")
