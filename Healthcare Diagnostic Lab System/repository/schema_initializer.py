from config.config import get_db_connection

def initialize_schema():
    # Establish a database connection
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        with open('repository/test_queries.sql', 'r') as file:
            query = file.read()

        # Split the file into individual SQL statements
        statements = query.split(';')

        # Execute each statement
        for statement in statements:
            statement = statement.strip()
            if statement:  # Only execute non-empty statements
                try:
                    cursor.execute(statement)
                    print(f"Executed: {statement[:50]}...")  # Log the first 50 characters of the statement
                except Exception as e:
                    print(f"Error executing statement: {statement[:50]}...")
                    print(f"Error: {e}")
                    continue  # Skip this statement and proceed to the next one

        # Commit changes to the database
        conn.commit()
        print("Database schema initialized successfully!")

    except FileNotFoundError:
        print("Error: SQL file 'test_queries.sql' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the cursor and connection are always closed
        cursor.close()
        conn.close()

# Call this function to initialize the schema
initialize_schema()
