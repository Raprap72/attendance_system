from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = 'attendance_system_secret_key'

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '22722243',
    'database': 'attendance_system'
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None

# Routes
@app.route('/')
def index():
    return render_template('index.html')

# DEPARTMENTS MANAGEMENT
@app.route('/departments')
def departments():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Departments ORDER BY DeptName")
        departments = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('departments.html', departments=departments)
    return render_template('departments.html', departments=[])

@app.route('/add_department', methods=['GET', 'POST'])
def add_department():
    if request.method == 'POST':
        dept_code = request.form['DeptCode']
        dept_name = request.form['DeptName']
        dept_head = request.form['DeptHead']
        dept_telno = request.form['DeptTelNo']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO Departments (DeptCode, DeptName, DeptHead, DeptTelNo) VALUES (%s, %s, %s, %s)",
                             (dept_code, dept_name, dept_head, dept_telno))
                conn.commit()
            except Error as e:
                print(f'Error adding department: {e}')
            finally:
                cursor.close()
                conn.close()
        return redirect(url_for('departments'))
    return render_template('add_department.html')

@app.route('/update_department/<dept_code>', methods=['GET', 'POST'])
def update_department(dept_code):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        
        if request.method == 'POST':
            dept_name = request.form['DeptName']
            dept_head = request.form['DeptHead']
            dept_telno = request.form['DeptTelNo']
            
            cursor.execute("UPDATE Departments SET DeptName = %s, DeptHead = %s, DeptTelNo = %s WHERE DeptCode = %s",
                         (dept_name, dept_head, dept_telno, dept_code))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('departments'))
        else:
            cursor.execute("SELECT * FROM Departments WHERE DeptCode = %s", (dept_code,))
            department = cursor.fetchone()
            cursor.close()
            conn.close()
            return render_template('update_department.html', department=department)
    
    return redirect(url_for('departments'))

@app.route('/delete_department/<dept_code>')
def delete_department(dept_code):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Departments WHERE DeptCode = %s", (dept_code,))
            conn.commit()
        except Error as e:
            print(f'Error deleting department: {e}')
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('departments'))

# EMPLOYEES MANAGEMENT
@app.route('/employees')
def employees():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT e.*, d.DeptName 
            FROM Employees e 
            JOIN Departments d ON e.DeptCode = d.DeptCode 
            ORDER BY e.EmpLName, e.EmpFName
        """)
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('employees.html', employees=employees)
    return render_template('employees.html', employees=[])

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        emp_id = request.form['EmpID']
        dept_code = request.form['DeptCode']
        emp_lname = request.form['EmpLName']
        emp_fname = request.form['EmpFName']
        emp_rate = request.form['EmpRatePerHour']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO Employees (EmpID, DeptCode, EmpLName, EmpFName, EmpRatePerHour) VALUES (%s, %s, %s, %s, %s)",
                             (emp_id, dept_code, emp_lname, emp_fname, emp_rate))
                conn.commit()
            except Error as e:
                print(f'Error adding employee: {e}')
            finally:
                cursor.close()
                conn.close()
        return redirect(url_for('employees'))
    
    # Get departments for dropdown
    conn = get_db_connection()
    departments = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT DeptCode, DeptName FROM Departments ORDER BY DeptName")
        departments = cursor.fetchall()
        cursor.close()
        conn.close()
    
    return render_template('add_employee.html', departments=departments)

@app.route('/update_employee/<int:emp_id>', methods=['GET', 'POST'])
def update_employee(emp_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        
        if request.method == 'POST':
            dept_code = request.form['DeptCode']
            emp_lname = request.form['EmpLName']
            emp_fname = request.form['EmpFName']
            emp_rate = request.form['EmpRatePerHour']
            
            cursor.execute("UPDATE Employees SET DeptCode = %s, EmpLName = %s, EmpFName = %s, EmpRatePerHour = %s WHERE EmpID = %s",
                         (dept_code, emp_lname, emp_fname, emp_rate, emp_id))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('employees'))
        else:
            cursor.execute("""
                SELECT e.*, d.DeptName 
                FROM Employees e 
                JOIN Departments d ON e.DeptCode = d.DeptCode 
                WHERE e.EmpID = %s
            """, (emp_id,))
            employee = cursor.fetchone()
            
            # Get departments for dropdown
            cursor.execute("SELECT DeptCode, DeptName FROM Departments ORDER BY DeptName")
            departments = cursor.fetchall()
            
            cursor.close()
            conn.close()
            return render_template('update_employee.html', employee=employee, departments=departments)
    
    return redirect(url_for('employees'))

@app.route('/delete_employee/<int:emp_id>')
def delete_employee(emp_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Employees WHERE EmpID = %s", (emp_id,))
            conn.commit()
        except Error as e:
            print(f'Error deleting employee: {e}')
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('employees'))

# ATTENDANCE RECORDING
@app.route('/attendance')
def attendance():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT a.*, e.EmpFName, e.EmpLName 
            FROM Attendance a 
            JOIN Employees e ON a.EmpID = e.EmpID 
            ORDER BY a.DateTimeIn DESC
        """)
        attendance_records = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('attendance.html', attendance_records=attendance_records)
    return render_template('attendance.html', attendance_records=[])

@app.route('/record_attendance', methods=['GET', 'POST'])
def record_attendance():
    if request.method == 'POST':
        emp_id = request.form['EmpID']
        datetime_in = request.form['DateTimeIn']
        datetime_out = request.form.get('DateTimeOut', '')
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            try:
                if datetime_out:
                    cursor.execute("INSERT INTO Attendance (EmpID, DateTimeIn, DateTimeOut) VALUES (%s, %s, %s)",
                                 (emp_id, datetime_in, datetime_out))
                else:
                    cursor.execute("INSERT INTO Attendance (EmpID, DateTimeIn) VALUES (%s, %s)",
                                 (emp_id, datetime_in))
                conn.commit()
            except Error as e:
                print(f'Error recording attendance: {e}')
            finally:
                cursor.close()
                conn.close()
        return redirect(url_for('attendance'))
    
    # Get employees for dropdown
    conn = get_db_connection()
    employees = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT EmpID, EmpFName, EmpLName 
            FROM Employees 
            ORDER BY EmpLName, EmpFName
        """)
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
    
    return render_template('record_attendance.html', employees=employees)

@app.route('/cancel_attendance/<int:record_no>')
def cancel_attendance(record_no):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Attendance WHERE RecordNo = %s", (record_no,))
            conn.commit()
        except Error as e:
            print(f'Error cancelling attendance: {e}')
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('attendance'))

# ATTENDANCE MONITORING BY EMPLOYEE
@app.route('/monitoring_employee', methods=['GET', 'POST'])
def monitoring_employee():
    employee_info = None
    attendance_records = []
    total_hours = 0
    salary = 0
    
    if request.method == 'POST':
        emp_id = request.form['EmpID']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            
            # Get employee info
            cursor.execute("""
                SELECT e.*, d.DeptName 
                FROM Employees e 
                JOIN Departments d ON e.DeptCode = d.DeptCode 
                WHERE e.EmpID = %s
            """, (emp_id,))
            employee_info = cursor.fetchone()
            
            if employee_info:
                # Get attendance records
                cursor.execute("""
                    SELECT RecordNo, EmpID, DateTimeIn, DateTimeOut,
                           TIMESTAMPDIFF(HOUR, DateTimeIn, COALESCE(DateTimeOut, NOW())) as TotalHours
                    FROM Attendance 
                    WHERE EmpID = %s 
                    ORDER BY DateTimeIn DESC
                """, (emp_id,))
                attendance_records = cursor.fetchall()
                
                # Calculate total hours and salary
                total_hours = sum(record['TotalHours'] for record in attendance_records if record['TotalHours'])
                salary = total_hours * employee_info['EmpRatePerHour']
            
            cursor.close()
            conn.close()
    
    return render_template('monitoring_employee.html', 
                         employee_info=employee_info, 
                         attendance_records=attendance_records,
                         total_hours=total_hours,
                         salary=salary,
                         date_generated=date.today())

# ATTENDANCE MONITORING BY DATE RANGE
@app.route('/monitoring_date_range', methods=['GET', 'POST'])
def monitoring_date_range():
    attendance_records = []
    total_hours = 0
    
    if request.method == 'POST':
        date_from = request.form['date_from']
        date_to = request.form['date_to']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT a.RecordNo, a.EmpID, a.DateTimeIn, a.DateTimeOut,
                       e.EmpFName, e.EmpLName,
                       TIMESTAMPDIFF(HOUR, a.DateTimeIn, COALESCE(a.DateTimeOut, NOW())) as TotalHours
                FROM Attendance a 
                JOIN Employees e ON a.EmpID = e.EmpID 
                WHERE DATE(a.DateTimeIn) BETWEEN %s AND %s 
                ORDER BY a.DateTimeIn DESC
            """, (date_from, date_to))
            attendance_records = cursor.fetchall()
            
            total_hours = sum(record['TotalHours'] for record in attendance_records if record['TotalHours'])
            
            cursor.close()
            conn.close()
    
    return render_template('monitoring_date_range.html', 
                         attendance_records=attendance_records,
                         total_hours=total_hours,
                         date_generated=date.today(),
                         date_from=request.form.get('date_from', ''),
                         date_to=request.form.get('date_to', ''))

if __name__ == '__main__':
    app.run(debug=True)
