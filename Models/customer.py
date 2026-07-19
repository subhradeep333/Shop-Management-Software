from Database.db_connection import get_connection


# Add Customer
def add_customer(name, phone, email):
    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO customers (customer_name, phone, email) VALUES (%s, %s, %s)"
    values = (name, phone, email)

    cursor.execute(query, values)
    connection.commit()

    print("Customer added successfully!")

    cursor.close()
    connection.close()


# View Customers
def view_customers():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM customers"
    cursor.execute(query)

    customers = cursor.fetchall()

    for customer in customers:
        print(customer)

    cursor.close()
    connection.close()


# Update Customer
def update_customer(customer_id, phone, email):
    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE customers SET phone=%s, email=%s WHERE customer_id=%s"
    values = (phone, email, customer_id)

    cursor.execute(query, values)
    connection.commit()

    print("Customer updated successfully!")

    cursor.close()
    connection.close()


# Delete Customer
def delete_customer(customer_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM customers WHERE customer_id=%s"
    cursor.execute(query, (customer_id,))

    connection.commit()

    print("Customer deleted successfully!")

    cursor.close()
    connection.close()


# Search Customer
def search_customer(name):
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM customers WHERE customer_name=%s"
    cursor.execute(query, (name,))

    customers = cursor.fetchall()

    for customer in customers:
        print(customer)

    cursor.close()
    connection.close()