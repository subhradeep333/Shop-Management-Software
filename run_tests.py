from Database.db_connection import get_connection, close_connection
from Modules import auth
import builtins
import sys


def test_db_connection():
    conn = get_connection()
    if conn is None:
        print("FAIL: DB connection returned None")
        return False
    close_connection(conn)
    print("PASS: DB connection")
    return True


def test_admin_row():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT username, password FROM admin")
    rows = cur.fetchall()
    cur.close()
    close_connection(conn)
    if not rows:
        print("FAIL: admin table empty")
        return False
    print(f"PASS: admin rows: {rows}")
    return True


def test_auth_login():
    inputs = iter(["admin", "admin123"])
    orig_input = builtins.input
    builtins.input = lambda prompt='': next(inputs)
    try:
        ok = auth.login()
    finally:
        builtins.input = orig_input

    if ok:
        print("PASS: auth.login() returned True")
        return True
    else:
        print("FAIL: auth.login() returned False")
        return False


def main():
    tests = [test_db_connection, test_admin_row, test_auth_login]
    results = [t() for t in tests]
    passed = sum(1 for r in results if r)
    total = len(results)
    print(f"\n{passed}/{total} tests passed")
    if passed != total:
        sys.exit(1)


if __name__ == "__main__":
    main()
