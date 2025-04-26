from datetime import datetime

class Menu:
    @staticmethod
    def get_patient_info():
        name = input("👤 Enter Patient Name: ").strip()
        dob = input("📅 Enter DOB (YYYY-MM-DD): ").strip()
        contact = input("📞 Enter Contact Number: ").strip()
        return (name, dob, contact)

    @staticmethod
    def get_test_request():
        while True:
            try:
                patient_id = int(input("🔹 Enter Patient ID: ").strip())
                test_id = int(input("🧪 Enter Test ID: ").strip())
                return (patient_id, test_id)
            except ValueError:
                print("❌ Please enter valid numeric IDs.")

    @staticmethod
    def get_test_result():
        while True:
            try:
                request_id = int(input("🧾 Enter Test Request ID: ").strip())
                value = float(input("📈 Enter Test Result Value: ").strip())
                return (request_id, value)
            except ValueError:
                print("❌ Please enter valid numeric values.")

    @staticmethod
    def get_patient_id():
        while True:
            try:
                return int(input("🔍 Enter Patient ID: ").strip())
            except ValueError:
                print("❌ Please enter a valid numeric ID.")

    @staticmethod
    def get_report_input():
        while True:
            try:
                return int(input("📄 Enter Patient ID for Report Generation: ").strip())
            except ValueError:
                print("❌ Invalid ID. Please enter a valid numeric Patient ID.")
