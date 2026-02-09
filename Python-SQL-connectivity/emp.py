### Employeee management System

# step_1 connect to mysql and create database
import mysql.connector
import pandas as pd
import numpy as np

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="7984455774sak"
)

cursor =conn.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS employee')
cursor.execute('Use employee')
print("Database employpee created and selected")

#step_2 :create_table

cursor.execute("""
CREATE TABLE IF NOT EXISTS emp_record_table (
    EMP_ID VARCHAR(10) PRIMARY KEY,
    FIRST_NAME VARCHAR(255),
    LAST_NAME VARCHAR(255),
    GENDER VARCHAR(10),
    ROLE VARCHAR(255),
    DEPT VARCHAR(255),
    EXP INT,
    COUNTRY VARCHAR(255),
    CONTINENT VARCHAR(255),
    SALARY FLOAT,
    EMP_RATING FLOAT,
    MANAGER_ID VARCHAR(10),
    PROJ_ID VARCHAR(10)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS proj_table (
    PROJECT_ID VARCHAR(10) PRIMARY KEY,
    PROJ_NAME VARCHAR(255),
    DOMAIN VARCHAR(255),
    START_DATE VARCHAR(20), -- Now stored as a string
    CLOSURE_DATE VARCHAR(20), -- Now stored as a string
    DEV_QTR VARCHAR(10),
    STATUS VARCHAR(50)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS data_science_team (
    EMP_ID VARCHAR(10) PRIMARY KEY,
    FIRST_NAME VARCHAR(255),
    LAST_NAME VARCHAR(255),
    GENDER VARCHAR(10),
    ROLE VARCHAR(255),
    DEPT VARCHAR(255),
    EXP INT,
    COUNTRY VARCHAR(255),
    CONTINENT VARCHAR(255)
);
""")
conn.commit()
print("\u2705 Tables created successfully!")

#step_3:function to insert csv Data into tables

def insert_csv_data(csv_file, table_name, dtype_mapping):
    try:
        # Read CSV with correct data types
        df = pd.read_csv(csv_file, dtype=dtype_mapping)
        df = df.replace({np.nan: None}) # Convert NaN to NULL

        for _, row in df.iterrows():
            placeholders = ", ".join(["%s"] * len(row))
            sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(sql, tuple(row))
        conn.commit()
        print(f"\u2705 Data from {csv_file} inserted into {table_name} successfully!")
    except Exception as e:
        print(f"\u274C Error inserting {csv_file}: {e}")


#step_4 : import csv data into tables
insert_csv_data("emp_record_table.csv", "emp_record_table", dtype_mapping={
"EMP_ID": str, "MANAGER_ID": str, "PROJ_ID":str
})
insert_csv_data("proj_table.csv", "proj_table", dtype_mapping={
"PROJECT_ID": str, "START_DATE": str, "CLOSURE_DATE": str  # Now treating as string
})

insert_csv_data("data_science_team.csv", "data_science_team", dtype_mapping={
"EMP_ID": str
})

# step_5: Close MYsql connection
cursor.close()
conn.close()
print("All tasks completed")
