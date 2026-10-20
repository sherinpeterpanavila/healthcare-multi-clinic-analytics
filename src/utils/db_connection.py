import mysql.connector
from src.config.database import DB_CONFIG

def get_connection(database):
    return mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG["port"],
        database=database
    )