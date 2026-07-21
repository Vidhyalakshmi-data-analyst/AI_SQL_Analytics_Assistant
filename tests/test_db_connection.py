from database.connection.db_connection import get_connection

def main():
    connection = get_connection()

    if connection:
        print("✅ Database connection successful!")

        cursor = connection.cursor()
        cursor.execute("SELECT version();")

        version = cursor.fetchone()

        print("\nPostgreSQL Version:")
        print(version[0])

        cursor.close()
        connection.close()

        print("\nConnection closed successfully.")

    else:
        print("Connection failed.")

if __name__ == "__main__":
    main()