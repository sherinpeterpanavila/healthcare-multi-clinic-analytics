import os
import pandas as pd

PROCESSED_DIR = "data/processed"

clinics = [
    "sunrise_clinic",
    "greenvalley_clinic",
    "citycare_clinic"
]


def validate_file(filename, required_columns):
    file_path = os.path.join(PROCESSED_DIR, filename)

    print(f"\nValidating: {filename}")

    if not os.path.exists(file_path):
        print("  ERROR: File does not exist")
        return False

    df = pd.read_csv(file_path)

    # Check required columns
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        print(f"  ERROR: Missing columns: {missing_columns}")
        return False

    # Check missing values
    missing_values = df[required_columns].isnull().sum()

    if missing_values.sum() > 0:
        print("  ERROR: Missing values found:")
        print(missing_values[missing_values > 0])
        return False

    print(f"  Rows: {len(df)}")
    print("  Validation: PASSED")

    return True


all_valid = True


# Patients
for clinic in clinics:
    result = validate_file(
        f"{clinic}_patients.csv",
        [
            "patient_id",
            "first_name",
            "last_name",
            "gender",
            "dob",
            "city",
            "phone"
        ]
    )

    if not result:
        all_valid = False


# Doctors
for clinic in clinics:
    result = validate_file(
        f"{clinic}_doctors.csv",
        [
            "doctor_id",
            "doctor_name",
            "specialty",
            "experience"
        ]
    )

    if not result:
        all_valid = False


# Appointments
for clinic in clinics:
    result = validate_file(
        f"{clinic}_appointments.csv",
        [
            "appointment_id",
            "patient_id",
            "doctor_id",
            "appointment_date",
            "diagnosis",
            "bill_amount"
        ]
    )

    if not result:
        all_valid = False


if all_valid:
    print("\nAll data validation checks PASSED.")
else:
    print("\nData validation FAILED.")