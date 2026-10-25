# Healthcare Multi-Clinic Analytics Platform

## Overview

An end-to-end AWS Data Engineering project that consolidates healthcare data from multiple clinic databases into a centralized analytics platform.

The project demonstrates a complete batch data pipeline using **MySQL, Python/Pandas, Amazon S3, AWS Glue, PySpark, Amazon Athena, and Power BI**.

The platform processes patient, doctor, and appointment data from three clinics and provides analytics including **clinic revenue, diagnosis revenue, appointment metrics, and Patient 360 insights**.

---

## Architecture

```text
┌─────────────────────────┐
│   MySQL Clinic DBs      │
│                         │
│  Sunrise Clinic         │
│  Green Valley Clinic    │
│  CityCare Clinic        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Python / Pandas         │
│                         │
│ Extract → Clean         │
│ Validate → Merge        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Amazon S3               │
│                         │
│ Raw / Processed Data    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ AWS Glue + PySpark      │
│                         │
│ Transform + Join        │
│ Curate Healthcare Data  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ S3 - Parquet            │
│ Curated Analytics Data  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Amazon Athena           │
│                         │
│ SQL Analytics           │
│ Patient 360             │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Power BI                │
│                         │
│ Healthcare Analytics    │
│ Patient 360 Dashboard   │
└─────────────────────────┘
```

---

## Business Problem

Healthcare organizations may operate multiple clinics with separate databases.

Analyzing data independently makes it difficult to obtain a unified view of:

- Patient activity
- Clinic performance
- Doctor performance
- Appointment trends
- Revenue
- Diagnosis distribution
- Patient history

This project builds a centralized analytics pipeline that combines data from multiple clinics and provides a unified reporting layer.

---

## Objectives

- Extract healthcare data from multiple MySQL clinic databases
- Clean and validate incoming data
- Remove duplicate business records
- Consolidate data from multiple clinics
- Build an AWS-based data lake using Amazon S3
- Transform data using AWS Glue and PySpark
- Store curated data in Parquet format
- Query analytical data using Amazon Athena
- Build Patient 360 analytics
- Create an interactive Power BI dashboard
- Demonstrate cloud-based batch ETL architecture

---

## Technology Stack

| Category | Technology |
|---|---|
| Source Database | MySQL 8.0 |
| Programming | Python |
| Data Processing | Pandas |
| Cloud Storage | Amazon S3 |
| ETL | AWS Glue |
| Distributed Processing | PySpark |
| File Format | Parquet |
| Query Engine | Amazon Athena |
| Visualization | Microsoft Power BI |
| Version Control | Git / GitHub |

---

## Data Sources

The project uses three clinic databases:

- Sunrise Clinic
- Green Valley Clinic
- CityCare Clinic

Each clinic contains:

- Patients
- Doctors
- Appointments

### Dataset

The pipeline initially processes **75 raw records** across the three clinics.

After data cleaning and deduplication, **45 clean records** are produced.

The current analytical dataset contains:

- 15 patients
- 15 doctors
- 15 appointments
- ₹27,300 total appointment revenue

---

## ETL Pipeline

### 1. Extract

Python extracts data from the three MySQL clinic databases and creates CSV files.

```text
MySQL
   ↓
Python Extraction
   ↓
data/raw/
```

### 2. Transform

The transformation layer:

- Removes duplicate business records
- Validates required columns
- Checks for missing values
- Adds clinic identifiers
- Merges data from all clinics

```text
data/raw/
   ↓
Cleaning
   ↓
Validation
   ↓
Merge
   ↓
data/processed/
```

### 3. Load to S3

Processed datasets are uploaded to Amazon S3.

```text
data/processed/
        ↓
Amazon S3
```

### 4. AWS Glue + PySpark

AWS Glue reads the processed CSV files from S3 and performs:

- Data transformation
- Patient joins
- Doctor joins
- Appointment enrichment
- Schema normalization

The curated output is stored as **Parquet**.

```text
S3 CSV
   ↓
AWS Glue
   ↓
PySpark
   ↓
S3 Parquet
```

### 5. Athena

Amazon Athena queries the curated Parquet data without requiring a traditional database server.

Analytical datasets include:

- Revenue by Clinic
- Revenue by Diagnosis
- Curated Appointments
- Patient 360

---

## Patient 360

The Patient 360 layer provides a unified view of each patient.

Metrics include:

- Clinic
- Patient ID
- Patient name
- Gender
- City
- Total appointments
- Total spend
- Average bill
- Last appointment
- Latest diagnosis
- Latest doctor
- Doctor count

The Patient 360 aggregation uses **clinic + patient ID** because patient IDs are local to each clinic.

This prevents records from different clinics with the same patient ID from being incorrectly combined.

---

## Power BI Dashboard

The final Power BI dashboard provides:

### KPI Metrics

- Total Patients: **15**
- Total Appointments: **15**
- Total Revenue: **₹27,300**
- Average Bill: **₹1,820**

### Visualizations

- Revenue by Clinic
- Revenue by Diagnosis
- Patient 360 Overview
- Clinic filter/slicer

The dashboard connects to Amazon Athena and provides interactive filtering by clinic.

---

## Key Analytics

### Revenue by Clinic

| Clinic | Revenue |
|---|---:|
| CityCare Clinic | ₹9,100 |
| Green Valley Clinic | ₹9,100 |
| Sunrise Clinic | ₹9,100 |

### Revenue by Diagnosis

| Diagnosis | Revenue |
|---|---:|
| Fracture | ₹10,500 |
| Migraine | ₹6,000 |
| Hypertension | ₹4,500 |
| Skin Allergy | ₹3,600 |
| Fever | ₹2,700 |

**Total Revenue: ₹27,300**

---

## Data Quality

The pipeline includes validation checks for:

- Required files
- Required columns
- Missing values
- Duplicate business records

Example validation command:

```powershell
py -m src.transform.validate_data
```

Expected result:

```text
All data validation checks PASSED.
```

---

## Project Structure

```text
healthcare-multi-clinic-analytics/
│
├── data/
│   ├── archive/
│   ├── processed/
│   └── raw/
│
├── dashboards/
│   └── Healthcare_Multi_Clinic_Analytics.pbix
│
├── docs/
│   └── architecture/
│
├── spark/
│   ├── jobs/
│   ├── transformations/
│   └── utils/
│
├── sql/
│   ├── queries/
│   ├── sample_data/
│   └── schema/
│
├── src/
│   ├── config/
│   ├── extract/
│   ├── generators/
│   ├── load/
│   ├── transform/
│   └── utils/
│
├── tests/
│
├── .gitignore
└── README.md
```

---

## Running the Local Pipeline

### Extract data

```powershell
py -m src.extract.extract_all
```

### Clean data

```powershell
py -m src.transform.clean_data
```

### Validate data

```powershell
py -m src.transform.validate_data
```

### Merge clinic data

```powershell
py -m src.transform.merge_clinics
```

### Run local analytics

```powershell
py -m src.transform.run_analytics
```

---

## AWS Components

### Amazon S3

Stores processed and curated healthcare datasets.

```text
s3://healthcare-multi-clinic-analytics/
```

### AWS Glue

Glue job:

```text
healthcare-clinic-pyspark-etl
```

The job transforms the processed clinic datasets and generates curated Parquet data.

### Amazon Athena

Athena queries the curated Parquet datasets stored in S3.

### Power BI

Power BI connects to Athena through the Amazon Athena ODBC connection and provides the final business dashboard.

---

## Security

Sensitive configuration such as database credentials is stored in environment variables.

Example:

```text
.env
```

The `.env` file is excluded from Git using `.gitignore`.

No passwords or AWS credentials should be committed to the repository.

---

## Future Enhancements

The current project focuses on a completed batch analytics pipeline.

Possible future improvements include:

- EventBridge + Lambda scheduling
- CloudWatch monitoring and alerting
- AWS DMS for CDC-based ingestion
- Kinesis for real-time healthcare events
- Apache Airflow orchestration
- Infrastructure as Code using Terraform
- CI/CD using GitHub Actions
- Predictive analytics / machine learning
- Data catalog and governance improvements

These are planned extensions and are **not represented as completed production features** in the current implementation.

---

## Project Status

**Completed MVP**

The core end-to-end pipeline has been implemented and tested:

```text
MySQL
  ↓
Python / Pandas
  ↓
Amazon S3
  ↓
AWS Glue / PySpark
  ↓
Parquet
  ↓
Amazon Athena
  ↓
Power BI
```

The project demonstrates practical experience with cloud data ingestion, ETL, distributed processing, data warehousing/querying, and business intelligence.

---

## Author

**Sherin Peter**

Senior Software Engineer transitioning into Data Engineering.

Focus areas:

- Python
- SQL
- AWS
- PySpark
- Data Engineering
- ETL / ELT
- Data Analytics
- Cloud Data Platforms