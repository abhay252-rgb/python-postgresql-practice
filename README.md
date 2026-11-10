# Python PostgreSQL Practice

A backend practice project built with Python, FastAPI, and PostgreSQL. This project focuses on connecting a Python application to a PostgreSQL database and building REST API endpoints to perform CRUD operations on employee records.

## Overview

The project demonstrates how a backend application communicates with a relational database, handles incoming API requests, validates data, and performs database operations.

It uses FastAPI to create API endpoints and Psycopg 3 to interact with PostgreSQL.

## Tech Stack

- Python – Backend programming
- FastAPI – REST API development
- PostgreSQL – Relational database
- Psycopg 3 – PostgreSQL database connection
- Pydantic – Request data validation
- python-dotenv – Environment variable management

## Features

- PostgreSQL database connection
- Create new employee records
- Retrieve all employee records
- Update employee salary using employee ID
- Delete employee records using employee ID
- Request data validation with Pydantic
- HTTP error handling for employee records that are not found
- Environment-based database configuration

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check backend status |
| GET | `/employees` | Retrieve all employees |
| POST | `/employees` | Create a new employee |
| PATCH | `/employees/{employee_id}` | Update employee salary |
| DELETE | `/employees/{employee_id}` | Delete an employee |

## Project Structure

```
python-postgresql-practice/
│
├── main.py
├── database_connection.py
├── .gitignore
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```
git clone https://github.com/abhay252-rgb/python-postgresql-practice.git
```

### 2. Navigate to the project directory

```
cd python-postgresql-practice
```

### 3. Create a virtual environment

```
python -m venv venv
```

Activate it on Windows:

```
venv\Scripts\activate
```

### 4. Install dependencies

```
pip install fastapi "uvicorn[standard]" "psycopg[binary]" python-dotenv
```

### 5. Create a PostgreSQL database

Create a database in PostgreSQL and run the following SQL to create the employee table:

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary INTEGER NOT NULL,
    age INTEGER NOT NULL
);
```

### 6. Configure environment variables

Create a `.env` file in the project root directory:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_postgresql_username
DB_PASSWORD=your_postgresql_password
```

Replace the database details with your own PostgreSQL configuration.

**Important:** Keep your `.env` file private. Never commit database credentials to GitHub.

### 7. Run the application

```
uvicorn main:app --reload
```

The application will run at: `http://127.0.0.1:8000`

## API Documentation

FastAPI provides interactive API documentation. After starting the application, open:

`http://127.0.0.1:8000/docs`

You can use the Swagger UI to explore the endpoints and send API requests.

## Learning Objectives

Through this project, I practised:

- Connecting Python applications with PostgreSQL
- Writing SQL queries through Python
- Building REST API endpoints using FastAPI
- Implementing CRUD operations
- Validating API request data with Pydantic
- Managing database configuration using environment variables
- Handling HTTP errors and database operations

## Project Status

This is a learning and practice project. It is part of my ongoing journey toward backend development, with more concepts and features to be explored and implemented.

---

Author: [abhay252-rgb](https://github.com/abhay252-rgb)
