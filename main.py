from Modules.auth import login

from Models.product import *
from Models.customer import *
from Models.sales import *
from Models.inventory import *

from Reports.report import *
from Reports.sales_chart import *


print("=" * 50)
print("      LOCAL SHOP MANAGEMENT SYSTEM")
print("=" * 50)

if login():

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Product Management")
        print("2. Customer Management")
        print("3. Sales Management")
        print("4. Inventory Management")
        print("5. Reports")
        print("6. Sales Charts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        # Product Menu
        if choice == "1":

            print("\n1. Add Product")
            print("2. View Products")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Search Product")

            option = input("Choose: ")

            if option == "1":
                name = input("Product Name: ")
                category = input("Category: ")
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                add_product(name, category, price, stock)

            elif option == "2":
                view_products()

            elif option == "3":
                pid = int(input("Product ID: "))
                price = float(input("New Price: "))
                stock = int(input("New Stock: "))
                update_product(pid, price, stock)

            elif option == "4":
                pid = int(input("Product ID: "))
                delete_product(pid)

            elif option == "5":
                name = input("Product Name: ")
                search_product(name)

        # Customer Menu
        elif choice == "2":

            print("\n1. Add Customer")
            print("2. View Customers")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. Search Customer")

            option = input("Choose: ")

            if option == "1":
                name = input("Customer Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                add_customer(name, phone, email)

            elif option == "2":
                view_customers()

            elif option == "3":
                cid = int(input("Customer ID: "))
                phone = input("New Phone: ")
                email = input("New Email: ")
                update_customer(cid, phone, email)

            elif option == "4":
                cid = int(input("Customer ID: "))
                delete_customer(cid)

            elif option == "5":
                name = input("Customer Name: ")
                search_customer(name)

        # Sales Menu
        elif choice == "3":

            print("\n1. Add Sale")
            print("2. View Sales")
            print("3. Delete Sale")
            print("4. Search Sale")

            option = input("Choose: ")

            if option == "1":
                pid = int(input("Product ID: "))
                cid = int(input("Customer ID: "))
                qty = int(input("Quantity: "))
                amount = float(input("Total Amount: "))
                add_sale(pid, cid, qty, amount)

            elif option == "2":
                view_sales()

            elif option == "3":
                sid = int(input("Sale ID: "))
                delete_sale(sid)

            elif option == "4":
                sid = int(input("Sale ID: "))
                search_sale(sid)

        # Inventory Menu
        elif choice == "4":

            print("\n1. Add Stock")
            print("2. Reduce Stock")
            print("3. View Stock")
            print("4. Low Stock")

            option = input("Choose: ")

            if option == "1":
                pid = int(input("Product ID: "))
                qty = int(input("Quantity: "))
                add_stock(pid, qty)

            elif option == "2":
                pid = int(input("Product ID: "))
                qty = int(input("Quantity: "))
                reduce_stock(pid, qty)

            elif option == "3":
                view_stock()

            elif option == "4":
                low_stock()

        # Reports
        elif choice == "5":

            print("\n1. Total Products")
            print("2. Total Customers")
            print("3. Total Sales")
            print("4. Sales Report")

            option = input("Choose: ")

            if option == "1":
                total_products()

            elif option == "2":
                total_customers()

            elif option == "3":
                total_sales()

            elif option == "4":
                sales_report()

        # Charts
        elif choice == "6":

            print("\n1. Product Stock Chart")
            print("2. Sales Amount Chart")
            print("3. Stock Distribution Chart")

            option = input("Choose: ")

            if option == "1":
                product_sales_chart()

            elif option == "2":
                sales_amount_chart()

            elif option == "3":
                stock_chart()

        elif choice == "7":
            print("Thank you for using the Shop Management System.")
            break

        else:
            print("Invalid Choice!")

else:
    print("Access Denied.")