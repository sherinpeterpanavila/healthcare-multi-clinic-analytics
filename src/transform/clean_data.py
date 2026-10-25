import os
import pandas as pd

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)


def clean_csv(filename, duplicate_columns):
    input_path = os.path.join(RAW_DIR, filename)
    output_path = os.path.join(PROCESSED_DIR, filename)

    print(f"Processing: {filename}")

    df = pd.read_csv(input_path)

    print(f"  Raw rows: {len(df)}")

    # Remove duplicate business records
    df = df.drop_duplicates(subset=duplicate_columns)

    print(f"  Clean rows: {len(df)}")

    df.to_csv(output_path, index=False)

    print(f"  Saved: {output_path}")


clinics = [
    "sunrise_clinic",
    "greenvalley_clinic",
    "citycare_clinic"
]


# -------------------------
# Patients
# -------------------------

for clinic in clinics:
    clean_csv(
        f"{clinic}_patients.csv",
        [
            "first_name",
            "last_name",
            "gender",
            "dob",
            "city",
            "phone"
        ]
    )


# -------------------------
# Doctors
# -------------------------

for clinic in clinics:
    clean_csv(
        f"{clinic}_doctors.csv",
        [
            "doctor_name",
            "specialty",
            "experience"
        ]
    )


# -------------------------
# Appointments
# -------------------------

for clinic in clinics:
    clean_csv(
        f"{clinic}_appointments.csv",
        [
            "patient_id",
            "doctor_id",
            "appointment_date",
            "diagnosis",
            "bill_amount"
        ]
    )


print("\nData cleaning completed successfully.")