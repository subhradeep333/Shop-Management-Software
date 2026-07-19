from Database.db_connection import get_connection
import matplotlib.pyplot as plt


# Bar Chart - Product Sales
def product_sales_chart():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT product_name, stock
    FROM products
    """

    cursor.execute(query)

    data = cursor.fetchall()

    product = []
    stock = []

    for row in data:
        product.append(row[0])
        stock.append(row[1])

    plt.bar(product, stock)

    plt.title("Product Stock")
    plt.xlabel("Products")
    plt.ylabel("Stock")

    plt.show()

    cursor.close()
    connection.close()


# Line Chart - Sales Amount
def sales_amount_chart():

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT sale_id, total_amount FROM sales"

    cursor.execute(query)

    data = cursor.fetchall()

    sale = []
    amount = []

    for row in data:
        sale.append(row[0])
        amount.append(row[1])

    plt.plot(sale, amount, marker="o")

    plt.title("Sales Amount")
    plt.xlabel("Sale ID")
    plt.ylabel("Amount")

    plt.show()

    cursor.close()
    connection.close()


# Pie Chart - Stock Distribution
def stock_chart():

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT product_name, stock FROM products"

    cursor.execute(query)

    data = cursor.fetchall()

    product = []
    stock = []

    for row in data:
        product.append(row[0])
        stock.append(row[1])

    plt.pie(stock, labels=product, autopct="%1.1f%%")

    plt.title("Stock Distribution")

    plt.show()

    cursor.close()
    connection.close()