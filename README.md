# 🏪 Local Shop Management System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![CLI](https://img.shields.io/badge/Interface-Command%20Line-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

A **CLI-based Local Shop Management Software** built using **Python** and **MySQL**. The application is designed to help small retail shops efficiently manage products, customers, inventory, and sales through a simple and user-friendly command-line interface.

---

# 📖 Table of Contents

- Overview
- Features
- Technology Stack
- Project Structure
- Database Design
- Installation
- Usage
- Future Enhancements
- Learning Outcomes
- Contributing
- License
- Author

---

# 📌 Overview

Managing a local retail shop manually can be difficult and time-consuming. This software automates daily business operations such as inventory tracking, customer management, sales processing, and report generation.

The application follows a modular architecture, making it easy to maintain, extend, and upgrade to a GUI version in the future.

---

# ✨ Features

## 🔐 Authentication

- Secure Admin Login
- Password Protected Access

---

## 📦 Product Management

- Add Products
- Update Products
- Delete Products
- View Products
- Search Products

---

## 👥 Customer Management

- Add Customers
- View Customer Details
- Search Customers
- Customer Purchase History

---

## 💰 Sales Management

- Generate Bills
- Automatic Total Calculation
- Store Sales Records
- Update Inventory Automatically

---

## 📦 Inventory Management

- Track Product Stock
- Low Stock Alerts
- Restock Products

---

## 📊 Reports

- Daily Sales Report
- Overall Sales Report
- Product-wise Sales
- Inventory Report

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| MySQL | Database Management |
| mysql-connector-python | Database Connectivity |
| CLI | User Interface |

---

# 📂 Project Structure

```
Local-Shop-Management-System/
│
├── .gitignore
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
│
├── database/
│   ├── __init__.py
│   ├── schema.sql
│   └── db_connection.py
│
├── modules/
│   ├── __init__.py
│   ├── auth.py
│   ├── product.py
│   ├── customer.py
│   ├── sales.py
│   ├── inventory.py
│   └── reports.py
│
├── utils/
│   ├── menu.py
│   ├── validation.py
│   ├── helper.py
│   └── bill.py
│
├── config/
│   └── config.py
│
├── data/
│   └── invoices/
│
└── screenshots/
```

---

# 🗄 Database Tables

- Admin
- Products
- Customers
- Sales
- Sales_Items

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/subhradeep333/Local-Shop-Management-System.git
```

---

## 2. Navigate to Project

```bash
cd Local-Shop-Management-System
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

### macOS / Linux

```bash
python3 -m venv .venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Create MySQL Database

```sql
CREATE DATABASE local_shop;
```

Import the schema:

```bash
mysql -u root -p local_shop < database/schema.sql
```

---

## 7. Configure Database

Update the database credentials inside:

```
database/db_connection.py
```

```python
HOST = "localhost"
USER = "root"
PASSWORD = "your_password"
DATABASE = "local_shop"
```

---

## 8. Run the Application

```bash
python main.py
```

---

# 💻 Sample Menu

```
=====================================
     LOCAL SHOP MANAGEMENT SYSTEM
=====================================

1. Product Management
2. Customer Management
3. Sales Management
4. Inventory Management
5. Reports
6. Exit

Enter Your Choice:
```

---

# 📷 Screenshots

```
screenshots/
│
├── login.png
├── dashboard.png
├── products.png
├── sales.png
└── reports.png
```

*(Add screenshots once the project is completed.)*

---

# 🚀 Future Enhancements

- ✅ Tkinter GUI Version
- Barcode Scanner Integration
- QR Code Billing
- GST Invoice Generation
- PDF Invoice Export
- Supplier Management
- Dashboard Analytics
- Multi-user Authentication
- Email Invoice Support
- Cloud Database Integration

---

# 🎯 Learning Outcomes

This project helped me gain practical experience in:

- Python Programming
- Object-Oriented Programming
- MySQL Database Design
- CRUD Operations
- SQL Queries
- Database Connectivity
- Modular Programming
- Exception Handling
- Inventory Management
- CLI Application Development

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## **Subhradeep Roy Chowdhury**

**BCA Student | Python Developer | Java Enthusiast**

🔗 GitHub: https://github.com/subhradeep333

🔗 LinkedIn: https://www.linkedin.com/in/subhradeep333

---

<p align="center">

⭐ If you like this project, consider giving it a Star!

</p>
