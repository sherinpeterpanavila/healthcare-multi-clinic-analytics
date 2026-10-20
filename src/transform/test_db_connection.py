from src.utils.db_connection import get_connection

connection = get_connection("sunrise_clinic")

print("✅ Connected Successfully!")

connection.close()

print("✅ Connection Closed!")