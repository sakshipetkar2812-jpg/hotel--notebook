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

# step-35:
# Function to determine job profile based on experience 
def get_job_profile(exp): 
    if exp <= 2: 
        return "JUNIOR DATA SCIENTIST" 
    elif 2 < exp <= 5: 
        return "ASSOCIATE DATA SCIENTIST"
    elif 5 < exp <= 10: 
        return "SENIOR DATA SCIENTIST" 
    elif 10 < exp <= 12: 
        return "LEAD DATA SCIENTIST" 
    elif 12 < exp <= 16: 
        return "MANAGER" 
    else: 
        return "UNKNOWN ROLE"

# Step 36: Fetch Employee Data 
cursor.execute(""" 
SELECT EMP_ID, FIRST_NAME, LAST_NAME, ROLE, EXP FROM emp_record_table; 
""") 
rows = cursor.fetchall() 

# Step 37: Process and Display Results 
print("\nEmployees and Their Expected Job Profiles:") 
print("EMP_ID | FIRST_NAME | LAST_NAME | ROLE | EXPERIENCE | EXPECTED_ROLE") 
print("-" * 80) 
for row in rows: 
    emp_id, first_name, last_name, role, exp = row 
    expected_role = get_job_profile(16) # Compute role in Python 
    print(f"{emp_id} | {first_name} | {last_name} | {role} | {exp} | {expected_role}") 

# Step 38: Close MySQL Connection 
cursor.close() 
conn.close()