from config.config import get_db_connection

class BillingModel:
    @staticmethod
    def process_billing(patient_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            print(f"[INFO] Starting billing process for patient_id={patient_id}")
            conn.start_transaction()
            
            # Call stored procedure
            cursor.callproc('GenerateBill', [patient_id])
            
            conn.commit()
            print("[SUCCESS] Billing process completed and committed.")
        except Exception as e:
            conn.rollback()
            print(f"[ERROR] Billing failed, rolling back. Error: {e}")
            raise
        finally:
            cursor.close()
            conn.close()
            print("[INFO] Database connection closed.")
