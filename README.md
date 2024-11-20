# Employee Management Application

This is a command-line application for managing employee data. Users can register, log in, and perform various operations on an employee database, such as adding, deleting, updating, searching, filtering, and viewing statistics.

## Features

- **User Registration and Login:**
  - Register with a username and password.
  - Log in with registered credentials.

- **Employee Management:**
  - Add new employees with details like ID, first name, last name, position, department, salary, start working date, and status.
  - Delete employees by ID.
  - Update employee details.
  - Search for employees by various attributes.
  - Filter employees based on department, salary, status, and start working date.
  - View statistics about employees, such as salary sums and averages.

## Requirements

- Python 3.x
- `tabulate` library for displaying data in tables

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the `tabulate` library using pip:

   ```bash
   pip install tabulate
   ```
3. Clone or download this repository to your local machine.

## Usage

1. Navigate to the directory containing the script.
2. Run the script using Python:
```bash
python capstone.py
```
3. Follow the on-screen instructions to either sign up or sign in.
4. Use the main menu to perform various operations on the employee database.

## Main Menu Options
1. Show List Employees: Display all employees in the database.
2. Add Employees: Add a new employee.
3. Delete Employees: Delete an employee by ID.
4. Update Employees: Update details of an existing employee.
5. Search Data Employees: Search for employees by ID, first name, last name, position, or department.
6. Filter Employees: Filter employees by department, salary, status, or start working date.
7. Stats Employees: View statistics such as the sum of salaries per department and average salaries.
8. Exit Program: Exit the application.

## Notes
- Usernames and passwords must be between 6 and 12 characters. Passwords must be alphanumeric.
- Employee IDs must be unique and greater than or equal to 1001.
- The application runs in a loop until the user chooses to exit.

## License
This `README.md` indicates that the project is free and open-source, allowing users to use, modify, and distribute it freely.