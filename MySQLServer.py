import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (adjust host, user, password as needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",            # change this if using another user
        password="Adewealth@61+2704"  # replace with your actual MySQL root password
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
