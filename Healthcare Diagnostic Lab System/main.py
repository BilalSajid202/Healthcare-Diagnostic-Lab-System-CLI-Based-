from controller.patient_controller import PatientController
from controller.test_controller import TestController
from controller.billing_controller import BillingController
from controller.report_controller import ReportController
from view.menu import Menu  

def main():
    patient_controller = PatientController()
    test_controller = TestController()
    billing_controller = BillingController()
    report_controller = ReportController()

    while True:
        print("""
        ***********************************
        Welcome to the Healthcare Lab System
        ***********************************

        Please choose one of the following options:

        1. Register Patient
        2. Request Test
        3. Enter Test Result (for authorized personnel)
        4. Generate Bill
        5. View Patient Info
        6. Generate Patient Report
        7. Help
        8. Exit

        ***********************************
        """)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            patient_controller.register()  # Register a new patient
        elif choice == '2':
            test_controller.assign_test()  # Assign test to patient
        elif choice == '3':
            test_controller.enter_result()  # Enter test results
        elif choice == '4':
            billing_controller.generate_bill()  # Generate billing info
        elif choice == '5':
            patient_controller.view_patient_info()  # View patient details
        elif choice == '6':
            patient_id = Menu.get_patient_id()  # 🔍 Ask for patient ID
            report_controller.generate_patient_report(patient_id)  # 📄 Generate report
        elif choice == '7':
            print("""
            **********************************
            Healthcare Lab System Help Guide
            **********************************
            1. Register Patient: Add a new patient to the system.
            2. Request Test: Assign a test to an existing patient.
            3. Enter Test Result: Authorized personnel can input test results.
            4. Generate Bill: Generate a bill based on tests requested for a patient.
            5. View Patient Info: View existing patient details (e.g., name, contact).
            6. Generate Patient Report: View full medical & billing history for a patient.
            7. Help: This guide on how to navigate the system.
            8. Exit: Exit the system and log out.
            **********************************
            """)
        elif choice == '8':
            print("Thank you for using the Healthcare Lab System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
