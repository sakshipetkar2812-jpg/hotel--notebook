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

# step-31  Create Stored Procedure to Retrieve Employees with More Than 3 Years of Experience 
cursor.execute(""" 
CREATE PROCEDURE IF NOT EXISTS GetExperiencedEmployees() 
BEGIN 
SELECT EMP_ID, FIRST_NAME, LAST_NAME, ROLE, EXP 
FROM emp_record_table 
WHERE EXP > 3; 
END; 
""") 
print("Stored procedure 'GetExperiencedEmployees' created successfully!")

#step-32 : Call the Stored Procedure 
cursor.callproc("GetExperiencedEmployees") 

# Step 33: Fetch and Display Results 
for result in cursor.stored_results(): 
    rows = result.fetchall() 
print("\nEmployees with More Than 3 Years of Experience:") 
print("EMP_ID | FIRST_NAME | LAST_NAME | ROLE | EXPERIENCE") 
print("-" * 60) 
for row in rows: 
    print(" | ".join(map(str, row))) 


# Step 34: Close MySQL Connection
cursor.close() 
conn.close()