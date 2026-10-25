import os
import pandas as pd

PROCESSED_DIR = "data/processed"
MERGED_DIR = "data/processed/merged"

os.makedirs(MERGED_DIR, exist_ok=True)

clinics = [
    "sunrise_clinic",
    "greenvalley_clinic",
    "citycare_clinic"
]


def merge_table(table_name):
    dataframes = []

    for clinic in clinics:
        filename = f"{clinic}_{table_name}.csv"
        file_path = os.path.join(PROCESSED_DIR, filename)

        df = pd.read_csv(file_path)

        # Add source clinic
        df["clinic_name"] = clinic

        dataframes.append(df)

    merged_df = pd.concat(dataframes, ignore_index=True)

    output_path = os.path.join(
        MERGED_DIR,
        f"all_clinics_{table_name}.csv"
    )

    merged_df.to_csv(output_path, index=False)

    print(f"{table_name}:")
    print(f"  Total rows: {len(merged_df)}")
    print(f"  Saved: {output_path}")


merge_table("patients")
merge_table("doctors")
merge_table("appointments")

print("\nClinic data merge completed successfully.")