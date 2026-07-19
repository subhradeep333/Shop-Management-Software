import matplotlib.pyplot as plt

def sales_chart():

    print("\n===== Sales Chart =====")
    print("1. Monthly Sales")
    print("2. Yearly Sales")

    choice = input("Enter your choice: ")

    labels = []
    sales = []

    if choice == "1":

        n = int(input("How many months do you want to enter? "))

        for i in range(n):
            month = input(f"Enter Month {i+1}: ")
            amount = float(input(f"Enter sales for {month}: ₹"))

            labels.append(month)
            sales.append(amount)

        plt.plot(labels, sales, marker="o")
        plt.title("Monthly Sales")
        plt.xlabel("Months")
        plt.ylabel("Sales Amount (₹)")
        plt.grid(True)
        plt.show()

    elif choice == "2":

        n = int(input("How many years do you want to enter? "))

        for i in range(n):
            year = input(f"Enter Year {i+1}: ")
            amount = float(input(f"Enter sales for {year}: ₹"))

            labels.append(year)
            sales.append(amount)

        plt.bar(labels, sales)

        plt.title("Yearly Sales")
        plt.xlabel("Years")
        plt.ylabel("Sales Amount (₹)")
        plt.show()

    else:
        print("Invalid Choice!")