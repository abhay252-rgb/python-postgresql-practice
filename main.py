import os

import psycopg
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI()

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    department: str = Field(min_length=2, max_length=50)
    salary: int = Field(gt=0)
    age: int = Field(gt=0, le=100)

class EmployeeUpdate(BaseModel):
    salary: int = Field(gt=0)

@app.get("/")
def home():
    return {"message": "My backend is running!"}

@app.get("/employees")
def get_employees():
    with psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, department, salary, age " 
                "FROM employees ORDER BY id"
            )
            rows = cursor.fetchall()
            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "department": row[2],
                    "salary": row[3],
                    "age": row[4],
                }
                for row in rows
            ]

@app.post("/employees", status_code=201)
def create_employee(employee: EmployeeCreate):
    with psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO employees (name, department, salary, age) VALUES (%s, %s, %s, %s) RETURNING id, name, department, salary, age",
                (employee.name,
                 employee.department,
                 employee.salary,
                 employee.age,
                 ),
            )
            row = cursor.fetchone()
        return {
            "id": row[0],
            "name": row[1],
            "department": row[2],
            "salary": row[3],
            "age": row[4]
        }

@app.patch("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeUpdate):
    with psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE employees
                SET salary = %s
                WHERE id = %s
                RETURNING id, name, department, salary, age""",
                (employee.salary, employee_id,),
            )
            row = cursor.fetchone()
            if row is None:
                raise HTTPException(
                    status_code=404,
                    detail="Employee not found"
                )
            return {
                "id": row[0],
                "name": row[1],
                "department": row[2],
                "salary": row[3],
                "age": row[4],
            }

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    with psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM employees
                WHERE id = %s
                RETURNING id, name, department, salary, age
                """,
                (employee_id,),
            )
            row = cursor.fetchone()
            if row is None:
                raise HTTPException(
                    status_code=404,
                    detail="Employee not found"
                )
            return {
                "message": "Employee deleted successfully",
                "employee": {
                    "id": row[0],
                    "name": row[1],
                    "department": row[2],
                    "salary": row[3],
                    "age": row[4],
                }
            }