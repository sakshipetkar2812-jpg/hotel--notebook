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

#step-42: Calculate Average Salary Distribution by Continent and Country 
cursor.execute(""" 
SELECT CONTINENT, COUNTRY, AVG(SALARY) AS AVG_SALARY 
FROM emp_record_table 
GROUP BY CONTINENT, COUNTRY; 
""") 
rows = cursor.fetchall() 

#step-43:  Display Average Salary Distribution 
print("\nAverage Salary Distribution by Continent and Country:") 
print("CONTINENT | COUNTRY | AVG_SALARY") 
print("-" * 50) 
for row in rows: 
    print(" | ".join(map(str, row))) 

#step_44:  Close MySQL Connection 
cursor.close() 
conn.close()