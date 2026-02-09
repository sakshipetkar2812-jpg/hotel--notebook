import mysql.connector
import pandas as pd
import numpy as np

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
cursor=conn.cursor()
print("connected to database")

# step_19: Create a view for employee with salaries greater than 6000 in different countries
cursor.execute("""
SELECT ROLE,MIN(SALARY) AS MIN_SALARY, MAX(SALARY) AS MAX_SALARY FROM emp_record_table group by ROLE;
""") 
rows= cursor.fetchall()

print("\n Minimum and Maximum salary")
print("Role | min | max")
print("-"*80)
for row in rows:
    print("|".join(map(str,row)))

#step_20 : Close MYsql connection
cursor.close()
conn.close()
print("All tasks completed")


