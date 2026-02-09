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

#step_17:Group Employes by department and fecth by their details along with Maximum Rating

cursor.execute("""
SELECT e.EMP_ID ,e.FIRST_NAME ,e.LAST_NAME, e.Role, e.DEPT, e.EMP_RATING,
   (SELECT MAX(EMP_RATING) FROM emp_record_table WHERE DEPT=E.DEPT)AS MAX_RATING 
   FROM emp_record_table e
   ORDER BY e.DEPT;
""")
rows=cursor.fetchall()

print("\n Employess Grouped by Department with maximum Rating:")
print("EMP_ID | FIRST_NAME | LAST_NAME | ROLE | DEPARTMENT | EMP_RATING | MAX_RATING")
print("-"*80)
for row in rows:
    print("|".join(map(str,row)))


# step_18:Close MYsql connection
cursor.close()
conn.close()
print("All tasks completed")






