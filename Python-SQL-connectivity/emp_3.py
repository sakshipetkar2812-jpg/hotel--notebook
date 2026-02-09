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

# step_12: Fetch empoylee who have subordinates
cursor.execute("""
SELECT MANAGER_ID,COUNT(*) AS num_reporters from emp_record_table
where MANAGER_ID IS NOT NULL
GROUP BY MANAGER_ID; 
""")
rows=cursor.fetchall()

# step_13:display results
print("\n Employess with subordinates:")
print("MANAGER_ID | NUM_REPOTERS")
print("-"*30)
for row in rows:
    print(f"{row[0]} | {row[1]}")

# step_14:Close MYsql connection
cursor.close()
conn.close()
print("All tasks completed")
 
