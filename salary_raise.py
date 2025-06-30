import os

# File name to store employee data
FILE_NAME = "employees.txt"

# Function to get employee input
def get_employee_input():
    try:
        name = input("Enter your name: ").strip()
        age = int(input("Enter your age (18-68): ").strip())

        if age < 18 or age > 68:
            raise ValueError("Age must be between 18 and 68.")

        designation = input("Enter designation (programmer/manager/tester): ").lower().strip()
        return name, age, designation

    except ValueError as e:
        print(f"Input Error: {e}")
        return None

# Function to get salary based on designation
def get_salary(designation):
    salary_structure = {
        'programmer': 25000,
        'manager': 30000,
        'tester': 20000
    }
    return salary_structure.get(designation)

# Save employee to file
def save_employee_to_file(emp):
    with open(FILE_NAME, 'a') as f:
        f.write(f"{emp['name']},{emp['age']},{emp['designation']},{emp['salary']}\n")

# Function to display employees
def display_employees():
    if not os.path.exists(FILE_NAME):
        print("\nNo employee records found.")
        return

    print("\nEmployee Details:")
    with open(FILE_NAME, 'r') as f:
        for line in f:
            name, age, designation, salary = line.strip().split(',')
            print(f"Name: {name}, Age: {age}, Designation: {designation.capitalize()}, Salary: ₹{salary}")

# Function to raise salary
def raise_salary():
    if not os.path.exists(FILE_NAME):
        print("No employee records to update.")
        return

    name_to_search = input("Enter the name of employee for raise: ").strip()

    try:
        hike_percent = float(input("Enter hike percentage (max 30%): ").strip())
        if hike_percent < 0 or hike_percent > 30:
            raise ValueError("Hike percent should be between 0 and 30.")

        updated = False
        lines = []

        with open(FILE_NAME, 'r') as f:
            for line in f:
                name, age, designation, salary = line.strip().split(',')
                if name.lower() == name_to_search.lower():
                    salary = int(salary)
                    new_salary = int(salary + (salary * hike_percent / 100))
                    lines.append(f"{name},{age},{designation},{new_salary}\n")
                    updated = True
                    print(f"Salary updated for {name}: ₹{new_salary}")
                else:
                    lines.append(line)

        with open(FILE_NAME, 'w') as f:
            f.writelines(lines)

        if not updated:
            print("Employee not found.")

    except ValueError as e:
        print(f"Input Error: {e}")

# Main menu-driven function
def main():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Create Employee Record")
        print("2. Display All Employees")
        print("3. Raise Salary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            while True:
                data = get_employee_input()
                if data:
                    name, age, designation = data
                    salary = get_salary(designation)

                    if salary is None:
                        print("Error: Invalid designation. Please enter programmer, manager, or tester.")
                        continue

                    emp = {
                        'name': name,
                        'age': age,
                        'designation': designation,
                        'salary': salary
                    }
                    save_employee_to_file(emp)

                cont = input("Do you want to add another employee? (y/n): ").lower()
                if cont != 'y':
                    break

        elif choice == '2':
            display_employees()

        elif choice == '3':
            raise_salary()

        elif choice == '4':
            print("Thank you for using the application. Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 4.")

# Run the program
main()
