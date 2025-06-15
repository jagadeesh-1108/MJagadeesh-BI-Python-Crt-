# Consider your a  HR operators managers in Vignan  software solutions , you are updating the employee databases,write a program to 
# 1)Tp add there even details in your company database which includes 
# employee name, employee ID, mail ID ,contact number, Date of joining , probatition period(just mention yes or no ),  notice period( just mention yes or no), designation ,salary
#  2) remove an employee from a company database based on employee ID 
# 3) check the  background verification status just mentioned as and print whether it is done or not ) for an employee
# 4) print the final List/Dictonary of the employee
# 5) Exit
# Employee Database Management System for Vignan Software Solutions

# Initialize employee database as a list of dictionaries
employee_db = [
    {
        'emp_id': 'VS001',
        'name': 'Rahul Sharma',
        'mail_id': 'rahul.sharma@vignanss.com',
        'contact': '9876543210',
        'doj': '2023-01-15',
        'probation': 'Yes',
        'notice_period': 'No',
        'designation': 'Software Engineer',
        'salary': 650000,
        'bg_verification': 'Done'
    },
    {
        'emp_id': 'VS002',
        'name': 'Priya Patel',
        'mail_id': 'priya.patel@vignanss.com',
        'contact': '8765432109',
        'doj': '2023-03-20',
        'probation': 'No',
        'notice_period': 'Yes',
        'designation': 'Senior Developer',
        'salary': 850000,
        'bg_verification': 'Pending'
    }
]

def add_employee():
    print("\n--- Add New Employee ---")
    emp_id = input("Enter Employee ID: ")
    
    # Check if employee ID already exists
    for emp in employee_db:
        if emp['emp_id'] == emp_id:
            print("Employee ID already exists!")
            return
    
    name = input("Enter Employee Name: ")
    mail_id = input("Enter Mail ID: ")
    contact = input("Enter Contact Number: ")
    doj = input("Enter Date of Joining (YYYY-MM-DD): ")
    probation = input("Is employee on probation? (Yes/No): ")
    notice_period = input("Is employee on notice period? (Yes/No): ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))
    bg_verification = input("Background Verification Status (Done/Pending): ")
    
    new_employee = {
        'emp_id': emp_id,
        'name': name,
        'mail_id': mail_id,
        'contact': contact,
        'doj': doj,
        'probation': probation,
        'notice_period': notice_period,
        'designation': designation,
        'salary': salary,
        'bg_verification': bg_verification
    }
    
    employee_db.append(new_employee)
    print(f"\nEmployee {name} added successfully!")

def remove_employee():
    print("\n--- Remove Employee ---")
    emp_id = input("Enter Employee ID to remove: ")
    
    for emp in employee_db:
        if emp['emp_id'] == emp_id:
            employee_db.remove(emp)
            print(f"Employee {emp['name']} (ID: {emp_id}) removed successfully!")
            return
    
    print(f"No employee found with ID: {emp_id}")

def check_bg_verification():
    print("\n--- Background Verification Check ---")
    emp_id = input("Enter Employee ID: ")
    
    for emp in employee_db:
        if emp['emp_id'] == emp_id:
            print(f"Background Verification Status for {emp['name']}: {emp['bg_verification']}")
            return
    
    print(f"No employee found with ID: {emp_id}")

def print_employee_list():
    print("\n--- Employee Database ---")
    print("{:<8} {:<20} {:<25} {:<12} {:<12} {:<10} {:<10} {:<20} {:<10} {:<10}".format(
        "ID", "Name", "Email", "Contact", "DOJ", "Probation", "Notice", "Designation", "Salary", "BG Check"
    ))
    
    for emp in employee_db:
        print("{:<8} {:<20} {:<25} {:<12} {:<12} {:<10} {:<10} {:<20} {:<10} {:<10}".format(
            emp['emp_id'],
            emp['name'],
            emp['mail_id'],
            emp['contact'],
            emp['doj'],
            emp['probation'],
            emp.get('notice_period', 'N/A'),
            emp['designation'],
            emp['salary'],
            emp['bg_verification']
        ))

def main_menu():
    while True:
        print("\n===== Vignan Software Solutions - HR Management System =====")
        print("1. Add New Employee")
        print("2. Remove Employee")
        print("3. Check Background Verification Status")
        print("4. View Employee Database")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            remove_employee()
        elif choice == '3':
            check_bg_verification()
        elif choice == '4':
            print_employee_list()
        elif choice == '5':
            print("Exiting HR Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main_menu()