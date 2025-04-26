# 🏥 Healthcare Diagnostic Lab System (CLI Based)

This is a beginner-friendly command-line Healthcare Lab Management System built using:

- ✅ Python 3
- ✅ MySQL (via MySQL Workbench)
- ✅ MVC Architecture
- ✅ Virtual Environment
- ✅ .env Configuration
- ✅ Stored Procedures, Triggers & Transactions

---

## 📁 Project Folder Structure
```
healthcare-lab-system/
│
├── config/              # DB connection setup using .env
│   └── config.py
│
├── controller/          # Control logic
│   ├── patient_controller.py
│   ├── test_controller.py
│   ├── billing_controller.py
│   └── report_controller.py
│
├── model/               # Handles CRUD operations
│   ├── patient_model.py
│   ├── test_model.py
│   └── billing_model.py
│
├── repository/          # SQL scripts and custom procedures
│   ├── schema_initializer.py
│   └── test_queries.sql
│
├── view/                # CLI Interface
│   └── menu.py
│
├── .env                 # DB credentials (MySQL)
├── main.py              # Project entry point
└── README.md            # You are here!
```

---

## ⚙️ Features

- 📝 Register new patients
- 🔍 View patient info by ID or Name
- 🧪 Schedule medical tests
- 📊 View test results and lab reports
- 💵 Generate and view patient bills
- 🔄 Uses stored procedures and triggers
- 💾 Automatically creates tables and schema (via `schema_initializer.py`)
- 🔐 Uses `.env` to keep DB credentials secure

---

## 🔐 .env Example

Create a `.env` file in the root with:

DB_HOST=localhost
DB_PORT=3307
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=healthcare_lab


> 🛑 You must manually create the `healthcare_lab` database in MySQL Workbench before running the app.

---

## 🧪 Testing DB Connection

Use the helper in `config/config.py` to check if your MySQL DB is connected:

```python
from config.config import test_db_connection

test_db_connection()
```

✅ If connected, you’ll see:
Database connection successful.

▶️ How to Run
✅ Create virtual environment (first time only):
python -m venv venv
▶️ Activate virtual environment:
venv\Scripts\activate
source venv/bin/activate
🧩 Install dependencies:
pip install mysql-connector-python python-dotenv
🚀 Run the app:
python main.py


🧠 What You Learn
Practical MVC pattern in Python
Python-MySQL integration (with mysql-connector-python)
SQL concepts like:
DDL, DML
Joins
Stored Procedures
Scalar Functions
Triggers (AFTER INSERT)
Transactions
Secure credential management with .env
Modular project organization
CLI interaction with real database operations

❤️ Contribution
This project was created for academic and learning purposes. Feel free to:

🌟 Fork the repo

✅ Add new modules (e.g., Doctor/Inventory modules)

🔧 Improve error handling and validations

🚀 Convert CLI to GUI or Flask-based app
