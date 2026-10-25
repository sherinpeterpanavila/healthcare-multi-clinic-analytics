from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, avg, round

spark = (
    SparkSession.builder
    .appName("HealthcareClinicAnalytics")
    .getOrCreate()
)

INPUT_PATH = "s3a://healthcare-multi-clinic-analytics/processed/"
OUTPUT_PATH = "s3a://healthcare-multi-clinic-analytics/analytics/"

appointments = spark.read.csv(
    INPUT_PATH + "all_clinics_appointments.csv",
    header=True,
    inferSchema=True
)

doctors = spark.read.csv(
    INPUT_PATH + "all_clinics_doctors.csv",
    header=True,
    inferSchema=True
)

patients = spark.read.csv(
    INPUT_PATH + "all_clinics_patients.csv",
    header=True,
    inferSchema=True
)

print("Appointments:")
appointments.show()

print("Doctors:")
doctors.show()

print("Patients:")
patients.show()

# Revenue by clinic
revenue_by_clinic = (
    appointments
    .groupBy("clinic_name")
    .agg(
        sum("bill_amount").alias("total_revenue"),
        count("*").alias("total_appointments"),
        round(avg("bill_amount"), 2).alias("average_bill")
    )
)

print("Revenue by Clinic:")
revenue_by_clinic.show()

# Revenue by diagnosis
revenue_by_diagnosis = (
    appointments
    .groupBy("diagnosis")
    .agg(
        count("*").alias("appointment_count"),
        sum("bill_amount").alias("total_revenue")
    )
    .orderBy("total_revenue", ascending=False)
)

print("Revenue by Diagnosis:")
revenue_by_diagnosis.show()

# Write analytics output as Parquet
revenue_by_clinic.write.mode("overwrite").parquet(
    OUTPUT_PATH + "revenue_by_clinic/"
)

revenue_by_diagnosis.write.mode("overwrite").parquet(
    OUTPUT_PATH + "revenue_by_diagnosis/"
)

print("PySpark analytics completed successfully.")

spark.stop()