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

# step-15: Fetch Employees from Healthcare and finance deparments using UNION
cursor.execute("""
SELECT EMP_ID,FIRST_NAME, DEPT from emp_record_table WHERE DEPT='Healthcare'
UNION
SELECT EMP_ID,FIRST_NAME,  DEPT from emp_record_table WHERE DEPT='finance';
""")
rows=cursor.fetchall()
print("\n Employess from healthcare and finance departments")
print("EMP_ID | FIRST_NAME | DEPT")
print('-'*60)
for row in rows:
    print("|".join(map(str,row)))

# step_16:Close MYsql connection
cursor.close()
conn.close()
print("All tasks completed")