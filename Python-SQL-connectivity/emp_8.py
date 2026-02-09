import mysql.connector
import pandas as pd
import numpy as np

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="7984455774sak",
    database="employee"
)
cursor=conn.cursor()
print("connected to database")

# step-25  Create a View for Employees with Salaries Greater Than 6000 in Different Countries 
cursor.execute(""" 
CREATE OR REPLACE VIEW high_salary_employees AS 
SELECT EMP_ID, FIRST_NAME, LAST_NAME, ROLE, COUNTRY, SALARY 
FROM emp_record_table 
WHERE SALARY > 6000; 
""") 
print("View 'high_salary_employees' created successfully!")

# step-26  Fetch and Display Data from the View 
cursor.execute("SELECT * FROM high_salary_employees;") 
rows = cursor.fetchall() 
 
print("\nEmployees with Salary Greater Than 6000:") 
print("EMP_ID | FIRST_NAME | LAST_NAME | ROLE | COUNTRY | SALARY") 
print("-" * 70) 
for row in rows: 
    print(" | ".join(map(str, row))) 

# Step 26: Close MySQL Connection 
cursor.close() 
conn.close()