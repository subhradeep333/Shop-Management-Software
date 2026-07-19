from Database.db_connection import get_connection


# Add Product
def add_product(name, category, price, stock):
    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO products (product_name, category, price, stock) VALUES (%s, %s, %s, %s)"
    values = (name, category, price, stock)

    cursor.execute(query, values)
    connection.commit()

    print("Product added successfully!")

    cursor.close()
    connection.close()


# View Products
def view_products():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM products"
    cursor.execute(query)

    products = cursor.fetchall()

    for product in products:
        print(product)

    cursor.close()
    connection.close()


# Update Product
def update_product(product_id, price, stock):
    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE products SET price=%s, stock=%s WHERE product_id=%s"
    values = (price, stock, product_id)

    cursor.execute(query, values)
    connection.commit()

    print("Product updated successfully!")

    cursor.close()
    connection.close()


# Delete Product
def delete_product(product_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM products WHERE product_id=%s"
    cursor.execute(query, (product_id,))
    connection.commit()

    print("Product deleted successfully!")

    cursor.close()
    connection.close()


# Search Product
def search_product(name):
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM products WHERE product_name=%s"
    cursor.execute(query, (name,))

    product = cursor.fetchall()

    for item in product:
        print(item)

    cursor.close()
    connection.close()