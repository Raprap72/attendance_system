# Employee Attendance Recording System

A comprehensive web-based employee attendance management system built with Python Flask and MySQL database for managing departments, employees, and attendance records.

## Features

### Department Management
- Add new departments with code, name, head, and contact information
- Edit department details
- Delete department records
- View all departments in the system

### Employee Management
- Add new employees with department assignment and hourly rates
- Edit employee information
- Delete employee records
- View all employees with department names
- Automatic department name display

### Attendance Recording
- Record employee check-in and check-out times
- Optional time-out field for ongoing shifts
- Cancel attendance records
- View all attendance records with employee names

### Attendance Monitoring (By Employee)
- Generate attendance reports for specific employees
- Display employee information and department
- Calculate total hours worked
- Calculate salary based on hourly rate
- Show individual attendance records with total hours

### Attendance Monitoring (Date Range)
- Generate attendance reports within specified date range
- Filter attendance records by date period
- Display total hours for all employees in the period
- Show employee names with attendance records

## Database Schema

### Departments Table
- `DeptCode` (PK, VARCHAR(10)): Department Code
- `DeptName` (VARCHAR(100)): Department Name
- `DeptHead` (VARCHAR(100)): Department Head
- `DeptTelNo` (VARCHAR(20)): Telephone Number

### Employees Table
- `EmpID` (PK, INT): Employee ID
- `DeptCode` (FK, VARCHAR(10)): Department Code
- `EmpLName` (VARCHAR(50)): Employee Last Name
- `EmpFName` (VARCHAR(50)): Employee First Name
- `EmpRatePerHour` (DECIMAL(10,2)): Hourly Rate

### Attendance Table
- `RecordNo` (PK, INT, AUTO_INCREMENT): Record Number
- `EmpID` (FK, INT): Employee ID
- `DateTimeIn` (DATETIME): Check-in Date/Time
- `DateTimeOut` (DATETIME): Check-out Date/Time (Optional)

## Requirements

- Python 3.7+
- MySQL 5.7+ or MySQL 8.0+
- Flask 2.3.3
- mysql-connector-python 8.1.0

## Installation

### 1. Clone or Download the Project
```bash
# Navigate to your desired directory
cd Desktop

# The project should be in: attendance_system/
```

### 2. Set up MySQL Database
```bash
# Login to MySQL
mysql -u root -p

# Execute the schema file
source database/schema.sql
```

### 3. Install Python Dependencies
```bash
# Navigate to project directory
cd attendance_system

# Install requirements
pip install -r requirements.txt
```

### 4. Configure Database Connection
Edit the `DB_CONFIG` in `app.py` if your MySQL credentials are different:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',  # Change if needed
    'database': 'attendance_system'
}
```

### 5. Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage

1. **Home Page**: Navigate to the main menu to access different modules
2. **Departments**: Add, edit, and delete department records
3. **Employees**: Register and manage employee information
4. **Attendance**: Record and manage employee attendance
5. **Monitoring (Employee)**: Generate employee-specific attendance reports
6. **Monitoring (Date Range)**: Generate date-range attendance reports

## Sample Data

The system comes with pre-loaded sample data for testing:
- 3 departments (HR, IT, Finance)
- 5 employees with different departments and rates
- 10 sample attendance records

## Project Structure

```
attendance_system/
|-- app.py                     # Main Flask application
|-- requirements.txt           # Python dependencies
|-- README.md                 # This file
|-- database/
|   |-- schema.sql            # MySQL database schema
|-- static/
|   |-- css/
|   |   |-- style.css         # Main stylesheet (embedded in base.html)
|-- templates/
|   |-- base.html             # Base template
|   |-- index.html            # Home page
|   |-- departments.html      # Departments management
|   |-- add_department.html   # Add department form
|   |-- update_department.html # Update department
|   |-- employees.html        # Employees management
|   |-- add_employee.html     # Add employee form
|   |-- update_employee.html  # Update employee
|   |-- attendance.html       # Attendance management
|   |-- record_attendance.html # Record attendance
|   |-- monitoring_employee.html # Monitoring by employee
|   |-- monitoring_date_range.html # Monitoring by date range
```

## Technical Features

- **Responsive Design**: Mobile-friendly interface
- **Modern UI**: Clean, professional design with CSS styling
- **Data Validation**: Form validation and error handling
- **Foreign Key Constraints**: Database integrity maintained
- **Time Calculations**: Automatic total hours calculation
- **Salary Calculations**: Automatic salary computation based on hours and rate
- **Date Range Filtering**: Flexible date-based reporting

## Security Notes

- This is a basic educational system
- In production, add authentication and authorization
- Use parameterized queries (already implemented)
- Add input validation and sanitization
- Implement HTTPS for production deployment

## Troubleshooting

### Database Connection Issues
- Ensure MySQL server is running
- Check database credentials in `app.py`
- Verify database was created using `schema.sql`

### Python Dependencies
- Use virtual environment: `python -m venv venv`
- Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
- Install: `pip install -r requirements.txt`

### Port Already in Use
- Change port in `app.py`: `app.run(debug=True, port=5001)`

## License

This project is for educational purposes. Feel free to modify and use for learning.
