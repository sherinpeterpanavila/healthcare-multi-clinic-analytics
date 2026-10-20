import pandas as pd

from src.utils.db_connection import get_connection

connection = get_connection("sunrise_clinic")

query = "SELECT * FROM patients"

df = pd.read_sql(query, connection)

print(df)

connection.close()