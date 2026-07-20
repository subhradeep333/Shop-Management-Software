from Database.db_connection import get_connection, close_connection

def login():
    print("\n===== ADMIN LOGIN =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    connection = get_connection()

    if connection is None:
        print("Database Connection Failed!")
        return False

    cursor = connection.cursor()

    query = "SELECT username, password FROM admin WHERE username = %s"

    cursor.execute(query, (username,))

    admin = cursor.fetchone()

    cursor.close()
    close_connection(connection)

    if admin is None:
        print("Username not found!")
        return False

    if password == admin[1]:
        print("Login Successful!")
        return True
    else:
        print("Incorrect Password!")
        return False


if __name__ == "__main__":
    login()