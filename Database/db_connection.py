import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="subhradeep3",
        database="local_shop"
    )
    return connection


def close_connection(connection):
    connection.close()


if __name__ == "__main__":
    conn = get_connection()
    print("✅ Database Connected Successfully!")

    close_connection(conn)
    print("✅ Database Connection Closed.")