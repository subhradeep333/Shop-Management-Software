# 🏪 Local Shop Management System

A Command-Line Interface (CLI) based **Local Shop Management System** developed using **Python** and **MySQL**. This project helps small local shop owners manage products, customers, sales, and inventory efficiently through a simple terminal interface.

---

## 📌 Features

- 📦 Product Management
  - Add new products
  - Update product details
  - Delete products
  - View all products
  - Search products

- 🛒 Inventory Management
  - Track available stock
  - Update stock after every sale
  - Low stock alerts

- 💰 Sales Management
  - Create new sales
  - Automatic bill generation
  - Calculate total amount
  - Update inventory automatically

- 👥 Customer Management
  - Add customers
  - View customer details
  - Purchase history

- 📊 Reports
  - Total sales report
  - Daily sales
  - Product-wise sales
  - Inventory report

- 🔐 Admin Login
  - Secure authentication
  - Password protected access

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| MySQL | Database |
| mysql-connector-python | Database Connectivity |
| CLI | User Interface |

---

## 📂 Project Structure

```
Local-Shop-Management-System/
│
├── database/
│   ├── schema.sql
│   └── sample_data.sql
│
├── modules/
│   ├── product.py
│   ├── customer.py
│   ├── sales.py
│   ├── inventory.py
│   ├── auth.py
│   └── database.py
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Local-Shop-Management-System.git
```

### 2. Navigate into the project

```bash
cd Local-Shop-Management-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the MySQL Database

```sql
CREATE DATABASE local_shop;
```

Import the SQL file:

```bash
mysql -u root -p local_shop < database/schema.sql
```

### 5. Configure Database

Update the MySQL credentials inside:

```python
database.py
```

```python
host="localhost"
user="root"
password="your_password"
database="local_shop"
```

### 6. Run the project

```bash
python main.py
```

---

## 📸 Sample Menu

```
=============================
 LOCAL SHOP MANAGEMENT SYSTEM
=============================

1. Product Management
2. Customer Management
3. Sales
4. Inventory
5. Reports
6. Exit

Enter Choice:
```

---

## 📊 Database Tables

- Products
- Customers
- Sales
- Sales_Items
- Inventory
- Admin

---

## 🚀 Future Enhancements

- GUI Version (Tkinter)
- Barcode Scanner Support
- Invoice PDF Generation
- GST Billing
- Supplier Management
- Multi-user Login
- Dashboard Analytics
- Cloud Database Integration
- QR Code Billing

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Python Programming
- MySQL Database Design
- CRUD Operations
- Database Connectivity using mysql-connector
- Modular Programming
- CLI Application Development
- Error Handling
- Inventory Management Logic

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Subhradeep Roy Chowdhury**

- GitHub: https://github.com/subhradeep333
- LinkedIn: https://www.linkedin.com/in/subhradeep333

---

### ⭐ If you found this project helpful, don't forget to Star this repository!
