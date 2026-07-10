import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Root@123",
    database="sunrise_clinic"
)
print("✅ Connected to MySQL Successfully!")

cursor = connection.cursor()

cursor.execute("SHOW TABLES")

print("\nTables in database:")
for table in cursor.fetchall():
    print(table[0])

cursor.close()
connection.close()

print("\nConnection Closed")