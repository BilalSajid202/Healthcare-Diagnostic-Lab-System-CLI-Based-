from config.config import get_db_connection

class TestModel:
    @staticmethod
    def schedule_test(patient_id, test_id):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Call the stored procedure to schedule the test
            cursor.callproc('ScheduleTest', [patient_id, test_id])
            conn.commit()
            print(f"✅ Test scheduled successfully for Patient ID {patient_id} with Test ID {test_id}")
        except Exception as e:
            # Handle any errors during scheduling
            print(f"❌ Error occurred while scheduling test: {e}")
        finally:
            # Ensure resources are released even in case of error
            cursor.close()
            conn.close()

    @staticmethod
    def insert_result(request_id, value):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Step 1: Check if the test request exists
            cursor.execute("SELECT id FROM TestRequests WHERE id = %s", (request_id,))
            result = cursor.fetchone()

            if result:
                # Step 2: Proceed to insert the result if the request exists
                query = "INSERT INTO Results (request_id, value) VALUES (%s, %s)"
                cursor.execute(query, (request_id, value))
                conn.commit()
                print(f"✅ Result inserted successfully for Test Request ID {request_id}")
            else:
                # Step 3: Inform the user if the request ID is invalid
                print(f"❌ Error: Test Request ID {request_id} does not exist.")
        except Exception as e:
            # Handle errors during the insertion of test results
            print(f"❌ Error occurred while inserting result: {e}")
        finally:
            # Ensure resources are released even in case of error
            cursor.close()
            conn.close()
