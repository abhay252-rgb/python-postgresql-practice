import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

connection = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

print("database connected successfully!")

cursor = connection.cursor()

cursor.execute(
    "SELECT name, salary FROM employees WHERE salary > 30000 ORDER BY salary DESC"
)

rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
