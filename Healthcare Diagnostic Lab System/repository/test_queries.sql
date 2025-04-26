-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS lab_db;

-- Step 2: Use the database
USE lab_db;

-- Step 3: Create Patients table
CREATE TABLE IF NOT EXISTS Patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    contact VARCHAR(20)
);

-- Step 4: Create Tests table
CREATE TABLE IF NOT EXISTS Tests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    test_name VARCHAR(100),
    price DECIMAL(10, 2) DEFAULT 50.00
);

-- Step 5: Create TestRequests table
CREATE TABLE IF NOT EXISTS TestRequests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    test_id INT,
    test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(id),
    FOREIGN KEY (test_id) REFERENCES Tests(id)
);

-- Step 6: Create Results table
CREATE TABLE IF NOT EXISTS Results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT,
    value FLOAT,
    FOREIGN KEY (request_id) REFERENCES TestRequests(id)
);

-- Step 7: Create Billing table
CREATE TABLE IF NOT EXISTS Billing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    bill_amount DECIMAL(10, 2),
    status ENUM('Paid', 'Unpaid') DEFAULT 'Unpaid',
    FOREIGN KEY (patient_id) REFERENCES Patients(id)
);
-- Create appointments table
CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    test_id INT,
    appointment_date DATETIME,
    FOREIGN KEY (patient_id) REFERENCES Patients(id),
    FOREIGN KEY (test_id) REFERENCES Tests(id)
);



-- Step 8: Stored Procedure to schedule a test
DELIMITER $$

CREATE PROCEDURE ScheduleTest(IN p_patient_id INT, IN p_test_id INT)
BEGIN
    INSERT INTO TestRequests (patient_id, test_id) 
    VALUES (p_patient_id, p_test_id);
END $$

DELIMITER ;

-- Step 9: Stored Procedure to generate a bill
DELIMITER $$

CREATE PROCEDURE GenerateBill(IN p_patient_id INT)
BEGIN
    DECLARE total_amount DECIMAL(10, 2);
    
    SELECT SUM(t.price) INTO total_amount
    FROM TestRequests tr
    JOIN Tests t ON tr.test_id = t.id
    WHERE tr.patient_id = p_patient_id;
    
    INSERT INTO Billing (patient_id, bill_amount, status)
    VALUES (p_patient_id, IFNULL(total_amount, 0.00), 'Unpaid');
END $$

DELIMITER ;

-- Step 10: View for patient test summary
CREATE OR REPLACE VIEW PatientTestSummary AS
SELECT 
    p.id AS patient_id,
    p.name,
    COUNT(tr.id) AS total_tests,
    IFNULL(SUM(b.bill_amount), 0) AS total_billed
FROM Patients p
LEFT JOIN TestRequests tr ON p.id = tr.patient_id
LEFT JOIN Billing b ON p.id = b.patient_id
GROUP BY p.id;

-- Step 11: Trigger to create unpaid bill after test scheduling
DELIMITER $$

CREATE TRIGGER CreateBillAfterTest
AFTER INSERT ON TestRequests
FOR EACH ROW
BEGIN
    DECLARE existing_bill_id INT;

    SELECT id INTO existing_bill_id
    FROM Billing
    WHERE patient_id = NEW.patient_id AND status = 'Unpaid'
    LIMIT 1;

    IF existing_bill_id IS NULL THEN
        INSERT INTO Billing (patient_id, bill_amount, status)
        VALUES (NEW.patient_id, 0.00, 'Unpaid');
    END IF;
END $$

DELIMITER ;
