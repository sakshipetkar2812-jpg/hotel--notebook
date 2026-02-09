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

#step_21:Rank Employess Based on Experience Without Using Rank()
cursor.execute("""
SELECT EMP_ID,FIRST_NAME, LAST_NAME ,ROLE,EXP FROM emp_record_table 
ORDER BY EXP DESC;
""")
rows=cursor.fetchall()
  
# step_22: Assign Ranks Manually in python
rank=1
previous_exp=None
rankings=[]
for row in rows:
    if previous_exp is None or row[4] !=previous_exp:
        rank+=1 
    rankings.append(row+(rank,))
    previous_exp=row[4]

# step_23: Display Results
print("\nEmployee rankings")
for row in rows:
    print("|    ".join(map(str,row)))

#STEP_24:Close MYsql connection
cursor.close()
conn.close()
print("All tasks completed")
 