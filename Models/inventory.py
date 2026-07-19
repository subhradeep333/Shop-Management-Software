from Database.db_connection import get_connection


# Increase Stock
def add_stock(product_id, quantity):
    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE products SET stock = stock + %s WHERE product_id = %s"
    cursor.execute(query, (quantity, product_id))

    connection.commit()

    print("Stock added successfully!")

    cursor.close()
    connection.close()


# Reduce Stock
def reduce_stock(product_id, quantity):
    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE products SET stock = stock - %s WHERE product_id = %s"
    cursor.execute(query, (quantity, product_id))

    connection.commit()

    print("Stock updated successfully!")

    cursor.close()
    connection.close()


# View Current Stock
def view_stock():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT product_id, product_name, stock FROM products"
    cursor.execute(query)

    products = cursor.fetchall()

    for product in products:
        print(product)

    cursor.close()
    connection.close()


# Check Low Stock
def low_stock(limit=5):
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT product_id, product_name, stock FROM products WHERE stock <= %s"
    cursor.execute(query, (limit,))

    products = cursor.fetchall()

    print("\nLow Stock Products")

    for product in products:
        print(product)

    cursor.close()
    connection.close()