import duckdb

con = duckdb.connect("data/healthcare.duckdb")

appointments = """
read_csv_auto(
    'data/processed/merged/all_clinics_appointments.csv'
)
"""

queries = {
    "Revenue by Clinic": f"""
        SELECT clinic_name,
               SUM(bill_amount) AS total_revenue
        FROM {appointments}
        GROUP BY clinic_name
        ORDER BY total_revenue DESC;
    """,

    "Appointments by Clinic": f"""
        SELECT clinic_name,
               COUNT(*) AS total_appointments
        FROM {appointments}
        GROUP BY clinic_name
        ORDER BY total_appointments DESC;
    """,

    "Average Bill by Clinic": f"""
        SELECT clinic_name,
               ROUND(AVG(bill_amount), 2) AS average_bill
        FROM {appointments}
        GROUP BY clinic_name
        ORDER BY average_bill DESC;
    """,

    "Revenue by Doctor": f"""
        SELECT clinic_name,
               doctor_id,
               COUNT(*) AS appointments,
               SUM(bill_amount) AS total_revenue
        FROM {appointments}
        GROUP BY clinic_name, doctor_id
        ORDER BY total_revenue DESC;
    """,

    "Top Diagnoses": f"""
        SELECT diagnosis,
               COUNT(*) AS appointment_count,
               SUM(bill_amount) AS total_revenue
        FROM {appointments}
        GROUP BY diagnosis
        ORDER BY appointment_count DESC;
    """
}

for title, query in queries.items():
    print(f"\n{'=' * 50}")
    print(title)
    print('=' * 50)

    result = con.execute(query).fetchdf()
    print(result.to_string(index=False))

con.close()