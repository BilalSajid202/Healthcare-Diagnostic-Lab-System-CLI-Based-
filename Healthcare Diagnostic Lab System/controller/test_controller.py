from model.test_model import TestModel
from view.menu import Menu
import mysql.connector
from config.config import get_db_connection

class TestController:

    def assign_test(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT id, name FROM Patients")
            patients = cursor.fetchall()

            print("\nSelect a patient by ID or Name:")
            for patient in patients:
                print(f"🧑 ID: {patient[0]} | Name: {patient[1]}")

            patient_input = input("🔹 Enter Patient ID or Name: ")
            if patient_input.isdigit():
                patient_id = int(patient_input)
            else:
                cursor.execute("SELECT id FROM Patients WHERE name = %s", (patient_input,))
                result = cursor.fetchone()
                if result:
                    patient_id = result[0]
                else:
                    print("❌ Patient not found.")
                    return

            cursor.execute("SELECT id, test_name FROM Tests")
            tests = cursor.fetchall()
            print("\n📋 Available Tests:")
            for test in tests:
                print(f"🧪 Test ID: {test[0]} | Name: {test[1]}")

            test_id = input("🔹 Enter Test ID: ")
            cursor.execute("SELECT id FROM Tests WHERE id = %s", (test_id,))
            if cursor.fetchone() is None:
                print("❌ Test not found.")
                return

            cursor.callproc('ScheduleTest', [patient_id, test_id])
            conn.commit()

            cursor.execute("SELECT LAST_INSERT_ID()")  # Get newly created TestRequest ID
            request_id = cursor.fetchone()[0]
            print(f"✅ Test scheduled successfully! Test Request ID: {request_id}")

        except Exception as e:
            print(f"❌ Error occurred: {e}")

        finally:
            cursor.close()
            conn.close()

    def enter_result(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Get the test request ID from the user
            request_id = input("Enter Test Request ID: ")

            # Check if the TestRequest exists
            cursor.execute("SELECT id FROM TestRequests WHERE id = %s", (request_id,))
            result = cursor.fetchone()

            if not result:
                print(f"❌ Test Request ID {request_id} does not exist.")
                return

            # Get the result value from the authorized personnel
            result_value = input("Enter the result value: ")

            # Insert the result using the model method
            TestModel.insert_result(request_id, result_value)

        except Exception as e:
            print(f"❌ Error occurred while entering the result: {e}")

        finally:
            cursor.close()
            conn.close()
