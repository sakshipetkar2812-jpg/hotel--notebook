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

#step-39 :  Calculate Bonus for Each Employee 
cursor.execute(""" 
SELECT EMP_ID, FIRST_NAME, LAST_NAME, ROLE, SALARY, EMP_RATING, 
(SALARY * 0.05 * EMP_RATING) AS BONUS 
FROM emp_record_table;
""") 
rows = cursor.fetchall()

#step-40:  Display Bonus Calculation Results 
print("\nEmployee Bonus Calculation:") 
print("EMP_ID | FIRST_NAME | LAST_NAME | ROLE | SALARY | EMP_RATING | BONUS") 
print("-" * 80) 
for row in rows: 
    print(" | ".join(map(str, row))) 

# Step 41: Close MySQL Connection 
cursor.close() 
conn.close() 