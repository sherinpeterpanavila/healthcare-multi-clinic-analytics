import os
import pandas as pd

from src.utils.db_connection import get_connection
from src.config.database import CLINICS
from src.utils.logger import logger

logger.info(f"Extract Phase Started ............")
TABLES = [
    "patients",
    "doctors",
    "appointments"
]

# Create data/raw folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

for clinic in CLINICS:

    logger.info(f"Processing clinic: {clinic}")

    try:
        connection = get_connection(clinic)

        for table in TABLES:

            try:
                query = f"SELECT * FROM {table}"

                df = pd.read_sql(query, connection)

                filename = f"data/raw/{clinic}_{table}.csv"

                df.to_csv(filename, index=False)

                logger.info(f"Exported {filename}")

            except Exception as e:
                logger.error(f"Failed to export table '{table}' from '{clinic}'. Error: {e}")
                print(f"❌ {clinic}.{table} -> {e}")

        connection.close()

    except Exception as e:
        logger.error(f"Database connection failed for '{clinic}'. Error: {e}")
        print(f"❌ Could not connect to {clinic}: {e}")

logger.info("ETL completed successfully.")
print("ETL completed.")