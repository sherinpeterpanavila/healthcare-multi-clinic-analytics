import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "port": int(os.getenv("MYSQL_PORT", "3306"))
}

CLINICS = [
    "sunrise_clinic",
    "greenvalley_clinic",
    "citycare_clinic"
]