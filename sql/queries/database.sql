CREATE DATABASE sunrise_clinic;
CREATE DATABASE greenvalley_clinic;
CREATE DATABASE citycare_clinic;


CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    dob DATE,
    city VARCHAR(50),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_name VARCHAR(100),
    specialty VARCHAR(100),
    experience INT
);

CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    diagnosis VARCHAR(200),
    bill_amount DECIMAL(10,2),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

INSERT INTO patients
(first_name,last_name,gender,dob,city,phone)
VALUES
('Akhil','Raj','Male','1995-03-10','Kochi','9876543210'),
('Neha','Paul','Female','1998-07-21','Trivandrum','9876543211'),
('Arjun','Nair','Male','1988-11-05','Kozhikode','9876543212'),
('Maria','Thomas','Female','1992-09-15','Kottayam','9876543213'),
('Kevin','George','Male','1999-02-12','Thrissur','9876543214');

INSERT INTO doctors (doctor_name, specialty, experience)
VALUES
('Dr. John Mathew','Cardiology',12),
('Dr. Susan George','Dermatology',8),
('Dr. Rahul Menon','Orthopedics',15),
('Dr. Anjali Nair','Pediatrics',10),
('Dr. Joseph Thomas','Neurology',18);

INSERT INTO appointments
(patient_id,doctor_id,appointment_date,diagnosis,bill_amount)
VALUES
(1,1,'2026-01-10','Hypertension',1500),
(2,2,'2026-01-11','Skin Allergy',1200),
(3,3,'2026-01-12','Fracture',3500),
(4,4,'2026-01-13','Fever',900),
(5,5,'2026-01-14','Migraine',2000);