from Database.db_connection import get_connection


# Add Sale
def add_sale(product_id, customer_id, quantity, total_amount):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO sales (product_id, customer_id, quantity, total_amount)
    VALUES (%s, %s, %s, %s)
    """

    values = (product_id, customer_id, quantity, total_amount)

    cursor.execute(query, values)
    connection.commit()

    print("Sale added successfully!")

    cursor.close()
    connection.close()


# View Sales
def view_sales():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM sales"
    cursor.execute(query)

    sales = cursor.fetchall()

    for sale in sales:
        print(sale)

    cursor.close()
    connection.close()


# Delete Sale
def delete_sale(sale_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM sales WHERE sale_id=%s"
    cursor.execute(query, (sale_id,))

    connection.commit()

    print("Sale deleted successfully!")

    cursor.close()
    connection.close()


# Search Sale
def search_sale(sale_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM sales WHERE sale_id=%s"
    cursor.execute(query, (sale_id,))

    sale = cursor.fetchall()

    for item in sale:
        print(item)

    cursor.close()
    connection.close()