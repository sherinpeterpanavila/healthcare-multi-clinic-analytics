-- 1. Total revenue by clinic

SELECT
    clinic_name,
    SUM(bill_amount) AS total_revenue
FROM read_csv_auto(
    'data/processed/merged/all_clinics_appointments.csv'
)
GROUP BY clinic_name
ORDER BY total_revenue DESC;