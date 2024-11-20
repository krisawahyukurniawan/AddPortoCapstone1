# import library date and tabulate, install tabulate before in terminal/bash
from datetime import date
from tabulate import tabulate

# User and employees database
user_database = [{'username':'Krisa1','password': 'Krisa123'}] # List to store user credentials
employees_database = [
                      {"ID": 996, "First Name": "John", "Last Name": "Doe", "Position": "Analyst", "Department": "Marketing", "Salary": 700, "Startworking": date(2022, 3, 10), "Status": "Active"},
                      {"ID": 997, "First Name": "Jane", "Last Name": "Smith", "Position": "Manager", "Department": "Sales", "Salary": 1200, "Startworking": date(2021, 8, 22), "Status": "Inactive"},
                      {"ID": 998, "First Name": "Emily", "Last Name": "Davis", "Position": "Designer", "Department": "Creative", "Salary": 900, "Startworking": date(2023, 1, 5), "Status": "Active"},
                      {"ID": 999, "First Name": "Michael", "Last Name": "Brown", "Position": "Developer", "Department": "IT", "Salary": 1100, "Startworking": date(2020, 11, 30), "Status": "Active"},
                      {"ID": 1000, "First Name" : "Krisa", "Last Name" : "Wahyu", "Position" : "Student", "Department" : "Data Science", "Salary" : 500, "Startworking" : date(2024,10,28),"Status": "Active"}] # List to store employee data

def show_welcome(): 
    # Display the welcome message and prompt the user to sign up or sign-in
    print('''
            ----------------------------------------------------
            Welcome to Employees Database Apps
            ----------------------------------------------------
            If you don't have an account, please sign up first.
            1. Sign Up
            2. Sign In
            ----------------------------------------------------
            Type 1 for Sign up, and type 2 for sign in.
          ''')
    user_input = None
    is_valid = False
    while not is_valid:
        user_input = input('Sign Up or Sign In: ')
        if user_input == '1':
            is_valid = True
            register(user_database)
        elif user_input == '2':
            is_valid = True
            sign_in()
        else:
            print('Enter number 1 or 2')

def sign_in(): 
    # Prompt the user to enter their username and password for sign-in
    username = input("Enter your username: ")
    password = input('Enter your password: ')
    login(username, password, user_database)
    
def login(username, password, user_dict): 
    # Validate user login credentials.
    user_index = search_username(username,user_dict)
    if user_index == -1:
        print('User is not registered.\nPlease, sign up first.')
        show_welcome()
    else:
        if password == user_dict[user_index]['password']:
            print('You successfully logged in.')
            display_main_menu()
        else:
            print('Invalid credentials.')
            show_welcome()
        
def search_username(username, user_dict): 
    # Search for a username in the user database.
    if user_dict != []:
        for index, user in enumerate(user_dict):
            if username == user['username']:
                return index
            elif index != len(user_dict) - 1:
                continue
            else:
                return -1
    else:
        return -1
    
def register(database): 
    # Register a new user with a username and password.
    username = input('Input your username: ')
    password = input('Input your password: ')
    is_valid = False
    user_index = search_username(username, database)
    while not is_valid:
        if user_index == -1:
            if len(username) >= 6 and len(username) <= 12:
                if len(password) >= 6 and len(password) <= 12 and password.isalnum():
                    password_confirmation = input('Input your password once again: ')
                    if password == password_confirmation:
                        is_valid = True
                        user = {'username':username,'password': password}
                        database.append(user)
                        print('User successfully registered')
                        show_welcome()
                    else:
                        print('Password is not match')
                        password_confirmation = input("Input your password again: ")
                else:
                    print('Password must contains 6-12 character and must be alphanumerical')
                    password = input('Input your password again: ')
            else:
                print('Username must contains 6-12 character')
                username = input('Input your username again: ')
        else:
            print('This account is already registered.')
            username = input('Input your username again: ')
    return is_valid

def display_employees():
    # Display all employees in the database in a tabular format.
    if employees_database == []:
        print('Your database is blank')
    else:
        headers = ["ID", "First Name", "Last Name", "Position", "Department", "Salary", "Startworking", "Status"]
        table = [[employee['ID'], employee['First Name'], employee['Last Name'], employee['Position'], employee['Department'], employee['Salary'], employee['Startworking'], employee['Status']] for employee in employees_database]
        print(tabulate(table, headers, tablefmt="pretty"))

def add_employees():
    # Add a new employee to database
    print('\nAdd Employees:')
    while True:
        try:
            id_employee = int(input("Enter new employee ID (minimum 1001): "))
            # Check if ID already exists in employees_database
            if any(emp['ID'] == id_employee for emp in employees_database):
                print("ID already exists. Please enter a unique ID.")
            elif id_employee < 1001:
                print("ID must be 1001 or greater. Please enter a valid ID.")
            else:
                break
        except ValueError:
            print("Invalid ID. Please enter a valid number.")

    while True:
        first_name_employee = input("Enter First Name: ")
        if all(c.isalpha() or c.isspace() for c in first_name_employee):
            first_name = first_name_employee.title()  # Mengubah menjadi title case
            break
        else:
            print("First Name must contain only letters.")

    while True:
        last_name_employee = input("Enter Last Name: ")
        if all(c.isalpha() or c.isspace() for c in last_name_employee):
            last_name = last_name_employee.title()
            break
        else:
            print("Last Name must contain only letters.")

    while True:
        position_employee = input('Enter position: ')
        if all(c.isalpha() or c.isspace() for c in position_employee):
            position = position_employee.title()
            break
        else:
            print("Position must contain only letters.")

    while True:
        department_employee = input('Enter department: ')
        if all(c.isalpha() or c.isspace for c in department_employee):
            department = department_employee.title()
            break
        else:
            print("Department must contain only letter.")

    while True:
        try:
            salary_employee = int(input('Input salary: '))
            break
        except ValueError:
            print("Invalid salary. Please enter a valid number.")

    while True:
        try:
            day_startworking = int(input('Input start working day: '))
            month_startworking = int(input('Input start working month: '))
            year_startworking = int(input('Input start working year: '))
            startworking_employee = date(year=year_startworking, month=month_startworking, day=day_startworking)
            break
        except ValueError:
            print("Invalid date. Please enter valid numbers for day, month, and year.")
    status_employee = "Active"


    # Add new employees to list
    employees_database.append({"ID":id_employee,"First Name": first_name, "Last Name": last_name, "Position": position, "Department": department, "Salary":salary_employee, "Startworking":startworking_employee, "Status": status_employee})
    print(f"{first_name_employee} {last_name_employee} is added to employees database.")

def delete_employees():
    # Delete an employee from the database by ID.
    display_employees()
    while True:
        try:
            id_employee = int(input("\nInput employee ID you want to delete: "))
            employee = next((emp for emp in employees_database if emp["ID"] == id_employee), None)
            if employee:
                employees_database.remove(employee)
                print(f"Employee with ID {id_employee} is deleted from employees list.")
                break
            else:
                print("ID not found. Please enter a valid ID.")
        except ValueError:
            print("Invalid ID. Please enter a valid number.")

def update_employee():
    # Update details of an existing employee.
    display_employees()

    while True:
        try:
            id = int(input("Input employee ID you want to update: "))
            employee = next((emp for emp in employees_database if emp["ID"] == id), None)
            if not employee:
                print("ID not found. Please enter a valid ID.")
                continue
            break
        except ValueError:
            print("Invalid ID. Please enter a valid number.")
    
    print('''
           Update your database employee
           ------------------------------
             1. Update First Name
             2. Update Last Name
             3. Update Position
             4. Update Department
             5. Update Salary
             6. Update Startworking
             7. Update Status 
           ------------------------------
           ''')
    try:
        update_choice = int(input('Input your update choice: '))
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 7.")
        return

    if update_choice == 1:
        while True:
            first_name = input('Enter new first name: ').title()
            if first_name.replace(" ","").isalpha():
                employee['First Name'] = first_name
                print('Employee first name updated successfully.')
                break
            else:
                print('First name must contain alphabetic characters. Please enter the data correctly.')
    elif update_choice == 2:
        while True:
            last_name = input('Enter new last name: ').title()
            if last_name.replace(" ","").isalpha():
                employee['Last Name'] = last_name
                print('Employee last name updated successfully.')
                break
            else:
                print('Last name must contains alphabetic characters. Please enter the data correctly.')
    elif update_choice == 3:
        while True:
            position = input('Enter new position: ').title()
            if position.replace(" ","").isalpha():
                employee['Position'] = position
                print('Employee position updated successfully.')
                break
            else:
                print('Last name must contains alphabetical characters. Please enter the data correctly.')
    elif update_choice == 4:
         while True:
            department = input('Enter new department: ').title()
            if department.replace(" ","").isalpha():
                employee['Department'] = department
                print('Employee department updated successfully.')
                break
            else:
                print('Department must contains alphabetical characters. Please enter the data correctly.')
    elif update_choice == 5:
        while True:
            try:
                employee['Salary'] = int(input('Enter new salary: '))
                print('Employee salary updated successfully.')
                break
            except ValueError:
                print("Invalid salary. Please enter a valid number.")
    elif update_choice == 6:
        while True:
            try:
                day = int(input('Enter start day: '))
                month = int(input('Enter start month: '))
                year = int(input('Enter start year: '))
                employee['Startworking'] = date(year=year, month=month, day=day)
                print("Employee startworking updated successfully.")
                break
            except ValueError:
                print("Invalid date. Please enter valid numbers for day, month, and year.")
    elif update_choice == 7:
         while True:
            status_input = input('Enter new status (True for Active, False for Inactive): ').strip().lower()
            if status_input == 'true':
                employee['Status'] = "Active"
                print('Employee status updated to Active.')
                break
            elif status_input == 'false':
                employee['Status'] = "Inactive"
                print('Employee status updated to Inactive.')
                break
            else:
                print('Invalid input. Please enter "True" for Active or "False" for Inactive.')
    else:
        print("Invalid choice. Please select a valid option.")

def search_employee():
    # Search for employees by ID, first name, last name, position, or department.
    if not employees_database:
        print('The employees data you search is not found. Try another keyword or ID again.')
        return
    
    print('''
            --------- Search Employee ---------
            1. Search by ID
            2. Search by First Name
            3. Search by Last Name
            4. Search by Position
            5. Search by Department
            -----------------------------------
          ''')
    try:
        search = int(input('Choose your search prefferences: '))
    except ValueError:
        print('Invalid input. Please enter a number between 1 and 4.')
        return
    # Search by ID
    if search == 1:
        try:
            employee_id = int(input("Enter employee ID: "))
            result = [emp for emp in employees_database if emp["ID"] == employee_id]
        except ValueError:
            print("Invalid ID. Please enter a valid number.")
            return
    # Search by First Name
    elif search == 2:
        employee_first_name = input('Enter employee first name: ').lower()
        result = [emp for emp in employees_database if emp['First Name'].lower() == employee_first_name]
    elif search == 3:
        employee_last_name = input('Enter employee last name: ').lower()
        result = [emp for emp in employees_database if emp['Last Name'].lower() == employee_last_name]
    # Search by Position
    elif search == 4:
        employee_position = input('Enter employee position:').lower()
        result = [emp for emp in employees_database if emp['Position'].lower() == employee_position]
    # Search by Department
    elif search == 5:
        employee_department = input('Enter employee department: ').lower()
        result = [emp for emp in employees_database if emp['Department'].lower() == employee_department]
    else:
        print('Invalid output. Please select a valid search option.')
        return

 # Display search results
    if result:
        print("\n---------- Search Results ----------")
        headers = ["ID", "First Name", "Last Name", "Position", "Department", "Salary", "Startworking", "Status"]
        table = [[employee['ID'], employee['First Name'], employee['Last Name'], employee['Position'], 
                  employee['Department'], employee['Salary'], employee['Startworking'], employee['Status']] 
                 for employee in result]
        print(tabulate(table, headers, tablefmt="pretty"))
    else:
        print("No matching employees found.")

def filter_employee():
    # Filter employees by department, salary, status, or start working date.
    print('''
        -----------Filtering Employee----------
        1. Filter by Department
        2. Filter by Salary
        3. Filter by Status
        4. Filter by Start Working Date
          ''')
    user_input = input('Enter number: ')
    # Filter by Department
    if user_input == '1':
        input_department = input('Enter employee department: ').lower()
        result = [emp for emp in employees_database if emp['Department'].lower() == input_department]
        if result:
            print("\n---------- Filter Results ----------")
            headers = ["ID", "First Name", "Last Name", "Department"]
            table = [[employee['ID'], employee['First Name'], employee['Last Name'], employee['Department']] for employee in result]
            print(tabulate(table, headers, tablefmt="pretty"))
        else:
            print("No matching employees found.")
    # Filter by Salary
    if user_input == '2':
        min_salary = int(input('Enter minimum salary: '))
        max_salary = int(input('Enter maximum salary: '))
        result = [emp for emp in employees_database if min_salary <= emp['Salary'] <= max_salary]
        if result:
            print("\n---------- Filter Results ----------")
            headers = ["ID", "First Name", "Last Name", "Salary"]
            table = [[employee['ID'], employee['First Name'], employee['Last Name'], employee['Salary']] for employee in result]
            print(tabulate(table, headers, tablefmt="pretty"))
        else:
            print("No matching employees found.")
    # Filter by Status
    if user_input == '3':
        input_status = input('Enter employee status (e.g, Active or Inactive): ').lower()
        result = [emp for emp in employees_database if emp['Status'].lower() == input_status]
        if result:
            print("\n---------- Filter Results ----------")
            headers = ["ID", "First Name", "Status"]
            table = [[employee['ID'], employee['First Name'], employee['Last Name'], employee['Status']] for employee in result]
            print(tabulate(table, headers, tablefmt="pretty"))
        else:
            print("No matching employees found.")
    # Filter by Startworking
    if user_input == '4':
        min_input_day = int(input('Filter working date from (1-31): '))
        min_input_month = int(input('Filter working month from (1-12): '))
        min_input_year = int(input('Filter working year from: '))
        min_input_date = date(min_input_year,min_input_month,min_input_day)
        max_input_day = int(input('Filter working date to (1-31): '))
        max_input_month = int(input('Filter working month to (1-12): '))
        max_input_year = int(input('Filter working year to: '))
        max_input_date = date(max_input_year,max_input_month,max_input_day)
        result = [emp for emp in employees_database if min_input_date <= emp['Startworking'] <= max_input_date]
        if result:
            print("\n---------- Filter Results ----------")
            headers = ["ID", "First Name", "Last Name", "Start Working"]
            table = [[employee['ID'], employee['First Name'], employee['Last Name'], employee['Startworking']] for employee in result]
            print(tabulate(table, headers, tablefmt="pretty"))
        else:
            print("No matching employees found.")
    elif not user_input:
        print('Invalid output. Please enter correct option.')

def stats_employee():
    # View statistics such as the sum of salaries per department and average salaries.
    print('''
        -----------Stats Employee----------
        1. Sum of employee salary per department
        2. Average salary per department
        3. Average salary per position
        4. Average salary all employees
          ''')
    user_input = input('Enter number : ')
    # Sum of employee salary per department
    if user_input == '1':
        department = input('Which department ?:  ')
        salaries = [emp['Salary'] for emp in employees_database if emp['Department'].title() == department.title()]
        if salaries:
            sum_salary = sum(salaries)
            print(f'Sum of employee salary from department {department} is {sum_salary}')
        else:
            print(f'No employees found in department {department}')
    # Average salary per department
    elif user_input == '2':
        department = input('Which department ?: ')
        salaries = [emp['Salary'] for emp in employees_database if emp['Department'].title() == department.title()]
        if salaries:
            average_department = sum(salaries) / len(salaries)
            print(f'Average of employee salary from department {department} is {average_department}')
        else:
            print(f'No employees found in department {department}')
    # Average salary per position
    elif user_input == '3':
        position = input('Which position?:')
        salaries = [emp['Salary'] for emp in employees_database if emp['Position'].title() == position.title()]
        if salaries:
            average_position = sum(salaries) / len(salaries)
            print(f'Average of employees salary from position {position} is {average_position}')
        else:
            print(f'No employees found with position {position}')
    # Average salary for all employees
    elif user_input == '4':
        if employees_database:
            avg_salary = sum(emp['Salary'] for emp in employees_database) / len(employees_database)
            print(f"Average Salary for All Employees: {avg_salary}")
        else:
            print("No employees to calculate average salary.")
    else:
        print('Invalid input. Please enter a number between 1 and 4.')


# Display Main Menu
def display_main_menu():
    # Display the main menu and prompt the user to select an option.
    while True:
        print('\n          ---------Main Menu---------')
        print('''
            1. Show List Employees
            2. Add Employees
            3. Delete Employees
            4. Update Employees
            5. Search Data Employees
            6. Filter Employees
            7. Stats Employees
            8. Exit Program
          ------------------------------''')
    
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Invalid output. Please enter a number between 1 and 8.")
            continue

        if choice == 1:
            display_employees()
        elif choice == 2:
            add_employees()
        elif choice == 3:
            delete_employees()
        elif choice == 4:
            update_employee()
        elif choice == 5:
            search_employee()
        elif choice == 6:
            filter_employee()
        elif choice == 7:
            stats_employee()
        elif choice == 8:
            print("""""
            ------------------
            Thank you! 
            Have a good time.
            ------------------
                  """)
            break
        else:
            print("""
                  -----------------------------------
                  Invalid input. Please enter a number between 1 and 8.
                  -----------------------------------
                  """)

# Running your main program
while True:
    show_welcome()