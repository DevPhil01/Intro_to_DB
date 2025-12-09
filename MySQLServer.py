# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL Server (connect to default 'mysql' database)
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',        # Replace with your MySQL username
            password='your_password'      # Replace with your MySQL password
            # Do not specify database here so we can create one
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function
if __name__ == "__main__":
    create_database()
