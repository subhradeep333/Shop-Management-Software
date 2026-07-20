from Database.db_connection import get_connection, close_connection

def login():
    """
    Authenticate the admin user.
    Returns:
        True  -> Login Successful
        False -> Login Failed
    """

    print("\n" + "=" * 40)
    print("         ADMIN LOGIN")
    print("=" * 40)

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    connection = get_connection()

    if connection is None:
        print("\n❌ Database Connection Failed!")
        return False

    cursor = connection.cursor()

    query = """
    SELECT username, password
    FROM admin
    WHERE username = %s
    """

    cursor.execute(query, (username,))

    admin = cursor.fetchone()

    cursor.close()
    close_connection(connection)

    if admin is None:
        print("\n❌ Username does not exist.")
        return False

    db_username, db_password = admin

    if password == db_password:
        print("\n✅ Login Successful!")
        return True
    else:
        print("\n❌ Incorrect Password.")
        return False


if __name__ == "__main__":
    login()