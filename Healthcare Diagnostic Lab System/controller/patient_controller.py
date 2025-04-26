from model.patient_model import PatientModel
from view.menu import Menu
import mysql.connector
from config.config import get_db_connection

class PatientController:

    def register(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Collect patient details from user
            name = input("Enter patient name: ")
            contact = input("Enter patient contact number: ")
            dob = input("Enter patient Date of Birth (YYYY-MM-DD): ")

            # Insert into Patients table
            query = "INSERT INTO Patients (name, contact, dob) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, contact, dob))
            conn.commit()
            print(f"✅ Patient {name} registered successfully!")

        except Exception as e:
            print(f"❌ Error occurred while registering patient: {e}")
        
        finally:
            cursor.close()
            conn.close()

    def view_patient_info(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Get Patient ID or Name
            patient_input = input("Enter Patient ID or Name: ")

            # Check if input is an ID (digit) or Name (string)
            if patient_input.isdigit():
                patient_id = int(patient_input)
                cursor.execute("SELECT id, name, contact, dob FROM Patients WHERE id = %s", (patient_id,))
            else:
                cursor.execute("SELECT id, name, contact, dob FROM Patients WHERE name = %s", (patient_input,))
            
            patient = cursor.fetchone()
            
            if patient:
                print(f"👤 Patient: {patient[1]}")
                print(f"📞 Contact: {patient[2]}")
                print(f"🎂 Date of Birth: {patient[3]}")
            else:
                print(f"❌ Patient with ID or Name '{patient_input}' not found.")
        
        except Exception as e:
            print(f"❌ Error occurred while retrieving patient information: {e}")
        
        finally:
            cursor.close()
            conn.close()
