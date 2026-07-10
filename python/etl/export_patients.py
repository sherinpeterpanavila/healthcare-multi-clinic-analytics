import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="sunrise_clinic"
)

query = "SELECT * FROM patients"

df = pd.read_sql(query, connection)

print(df)

df.to_csv("data/raw/patients.csv", index=False)

print("Patients exported successfully!")

connection.close()