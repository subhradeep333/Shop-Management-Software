from Database.db_connection import get_connection


# Total Products
def total_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")

    total = cursor.fetchone()

    print("Total Products:", total[0])

    cursor.close()
    connection.close()


# Total Customers
def total_customers():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")

    total = cursor.fetchone()

    print("Total Customers:", total[0])

    cursor.close()
    connection.close()


# Total Sales Amount
def total_sales():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(total_amount) FROM sales")

    total = cursor.fetchone()

    print("Total Sales Amount:", total[0])

    cursor.close()
    connection.close()


# View Sales Report
def sales_report():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM sales")

    sales = cursor.fetchall()

    print("\n------ Sales Report ------")

    for sale in sales:
        print(sale)

    cursor.close()
    connection.close()