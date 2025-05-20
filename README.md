# Volunteer Data Management System  
*A Prototype for Data Governance at Health Service Center 41 Khlong Toei*

## 📌 Project Context

This system was developed as part of the DSI324 – Data Governance Project course. The aim was to improve how data from **volunteer drug prevention efforts** is collected, validated, and secured at **Health Service Center 41 Khlong Toei**, a public health unit in a high-density urban community with ongoing drug-related challenges.

Previously, data was recorded on paper forms and manually re-entered into excel, which created issues such as:
- Inconsistent formats  
- Data duplication  
- Limited traceability  
- Weak access control (e.g., former staff still able to access sensitive data)

---

## 🛠️ System Overview

The developed prototype is a web-based application that improves the data workflow through:

- **Individual user login system** (username & password)  
- **Access control by role** (admin, user (staff), external viewers)  
- **Audit logging** for accountability  
- **Structured data input** via web forms  
- **Secure backend database** using MySQL  
- **Containerized environment** with Docker Compose  

---

## 🚀 How to Run the System

1. Make sure you have completed and are running the data container from the following project:  
   ▶️ **[dsi321_2025 (GitHub)](https://github.com/khwkong/dsi321_2025)**  
   This project provides essential data services that this system depends on.

2. Clone this repository and build the container:

```bash
docker-compose up --build
```

3. Visit the application at:  
   [http://localhost:8501](http://localhost:8501)

> The MySQL database will initialize automatically using `init.sql`.

---

## 🔐 User Setup & Access

Before you can access the Streamlit web interface, you **must create a user account** using the `create_acc_manual.py` script.

```bash
python create_acc_manual.py
```

You will be prompted to enter:
- Username
- Password
- Role (`admin`, `user`, or `visitor`)

### 🔑 Role-Based Access
- **Admin**: Full access to manage data, accounts, and view logs  
- **User**: Can input and manage volunteer activity data  
- **Visitor**: Can view only limited public information (read-only)  

> Make sure each role is used appropriately for security and governance compliance.

---

## 📂 Folder Structure

```text
dsi324-volunteer-system/
├── app.py                  # Main Streamlit entry point
├── create_acc_manual.py    # Manual script to create user accounts
├── modules/                # Streamlit page modules
│   ├── login.py
│   └── check_volunteer.py
│   └── search_volunteer.py
│   └── ...
├── utils/
│   └── db.py               # DB connection and utility functions
├── init.sql                # SQL schema initialization
├── Dockerfile              # Streamlit container build file
├── docker-compose.yml      # Full stack config (Streamlit + MySQL)
├── requirements.txt        # Python dependencies
└── .streamlit/
    └── config.toml         # Streamlit theme and settings
```

---

## 🛡️ Data Governance Implementation

| Area                  | Applied Practice |
|-----------------------|------------------|
| **Data Quality**      | Standardized input forms, validation |
| **Data Integrity**    | SQL schema enforcement, typed inputs |
| **Data Security**     | Role-based access, password control |
| **Transparency**      | Log history, clear data flow |
| **Lifecycle**         | Covers creation, view, update, and deletion |

---

This project demonstrates how data governance principles can be applied in real-world public health work to improve data quality, security, and operational efficiency.  
By implementing a role-based, auditable, and modular system, we aim to set a foundation for more scalable and trustworthy community health data management in the future.

Thank you for your interest in this project.  
We hope this system serves as a meaningful starting point for applying data governance in practical community health contexts.  
Feel free to explore, adapt, and build upon it to support your own learning or initiatives in data-driven public service.