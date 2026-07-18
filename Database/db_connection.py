import mysql.connector
from mysql.connector import Error

HOST = "localhost"
USER = "root"
PASSWORD = "subhradeep3"      
DATABASE = "local_shop"



def get_connection():
    """
    Creates and returns a connection to the MySQL database.
    Returns:
        connection object if successful
        None if connection fails
    """
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print("\n❌ Database Connection Failed!")
        print(f"Error: {e}")
        return None



def close_connection(connection):
    """
    Closes the database connection safely.
    """
    if connection is not None and connection.is_connected():
        connection.close()


if __name__ == "__main__":
    conn = get_connection()

    if conn:
        print("✅ Connected to MySQL successfully!")
        close_connection(conn)
        print("🔒 Connection Closed.")