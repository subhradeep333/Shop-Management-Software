from Database.db_connection import get_connection, close_connection
import os


def run_schema_and_seed():
    base = os.path.dirname(__file__)
    schema_path = os.path.join(base, "Database", "schema.sql")

    if not os.path.exists(schema_path):
        print("Schema file not found:", schema_path)
        return

    with open(schema_path, "r") as f:
        sql = f.read()

    conn = get_connection()
    if conn is None:
        print("Failed to connect to the database. Aborting.")
        return

    cursor = conn.cursor()

    statements = [s.strip() for s in sql.split(";") if s.strip()]

    for stmt in statements:
        try:
            cursor.execute(stmt)
        except Exception as e:
            # Some statements (like CREATE DATABASE/USE) may be environment-specific.
            print(f"Notice: couldn't execute statement: {e}")

    conn.commit()

    # Seed admin user
    username = input("Admin username [admin]: ") or "admin"
    password = input("Admin password [admin]: ") or "admin"

    try:
        cursor.execute("SELECT admin_id FROM admin WHERE username = %s", (username,))
        if cursor.fetchone():
            print("Admin user already exists. Skipping insert.")
        else:
            cursor.execute(
                "INSERT INTO admin (username, password) VALUES (%s, %s)", (username, password)
            )
            conn.commit()
            print("Admin user created successfully.")
    except Exception as e:
        print("Failed to seed admin user:", e)

    cursor.close()
    close_connection(conn)


if __name__ == "__main__":
    run_schema_and_seed()
