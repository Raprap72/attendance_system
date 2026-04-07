-- Employee Attendance Recording System Database Schema
-- Create database
CREATE DATABASE IF NOT EXISTS attendance_system;
USE attendance_system;

-- Drop tables if they exist (to start fresh)
DROP TABLE IF EXISTS Attendance;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

-- Departments Table
CREATE TABLE Departments (
    DeptCode VARCHAR(10) PRIMARY KEY,
    DeptName VARCHAR(100) NOT NULL,
    DeptHead VARCHAR(100) NOT NULL,
    DeptTelNo VARCHAR(20) NOT NULL
);

-- Employees Table
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    DeptCode VARCHAR(10) NOT NULL,
    EmpLName VARCHAR(50) NOT NULL,
    EmpFName VARCHAR(50) NOT NULL,
    EmpRatePerHour DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (DeptCode) REFERENCES Departments(DeptCode)
);

-- Attendance Table
CREATE TABLE Attendance (
    RecordNo INT AUTO_INCREMENT PRIMARY KEY,
    EmpID INT NOT NULL,
    DateTimeIn DATETIME NOT NULL,
    DateTimeOut DATETIME,
    FOREIGN KEY (EmpID) REFERENCES Employees(EmpID)
);

-- Insert sample data
INSERT INTO Departments (DeptCode, DeptName, DeptHead, DeptTelNo) VALUES
('HR', 'Human Resources', 'John Smith', '123-456-7890'),
('IT', 'Information Technology', 'Jane Doe', '123-456-7891'),
('FIN', 'Finance', 'Mike Johnson', '123-456-7892');

INSERT INTO Employees (EmpID, DeptCode, EmpLName, EmpFName, EmpRatePerHour) VALUES
(1001, 'HR', 'Cruz', 'Juan', 150.00),
(1002, 'IT', 'Santos', 'Maria', 200.00),
(1003, 'FIN', 'Reyes', 'Carlos', 180.00),
(1004, 'HR', 'Garcia', 'Ana', 160.00),
(1005, 'IT', 'Lopez', 'Pedro', 220.00);

INSERT INTO Attendance (EmpID, DateTimeIn, DateTimeOut) VALUES
(1001, '2024-01-15 08:00:00', '2024-01-15 17:00:00'),
(1002, '2024-01-15 08:30:00', '2024-01-15 17:30:00'),
(1003, '2024-01-15 09:00:00', '2024-01-15 18:00:00'),
(1001, '2024-01-16 08:00:00', '2024-01-16 17:00:00'),
(1002, '2024-01-16 08:30:00', '2024-01-16 17:30:00'),
(1004, '2024-01-16 09:00:00', '2024-01-16 18:00:00'),
(1005, '2024-01-17 08:00:00', '2024-01-17 17:00:00'),
(1003, '2024-01-17 08:30:00', '2024-01-17 17:30:00'),
(1001, '2024-01-17 09:00:00', '2024-01-17 18:00:00'),
(1004, '2024-01-18 08:00:00', '2024-01-18 17:00:00');

-- Verify tables were created successfully
SELECT 'Database setup completed successfully' as status;
SELECT COUNT(*) as department_count FROM Departments;
SELECT COUNT(*) as employee_count FROM Employees;
SELECT COUNT(*) as attendance_count FROM Attendance;
