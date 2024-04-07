import csv
import os
import sys

print("welcome to your app, admin please enter your username and password for adding employees")

def admin_login():
    username = input("Enter your username (admin): ")
    password = input("Enter your password (admin): ")
    if username.lower() == "admin" and password == "12345":
        return True
    else:
        return False

def add_employee():
    file_exists = os.path.isfile('employees.csv') and os.path.getsize('employees.csv') > 0
    with open('employees.csv', 'a', newline='') as csvfile:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        while True:
            employee_username = input("Enter the employee's username: ")
            employee_password = input("Enter the employee's password: ")
            if len(employee_password) <= 7:
                print("Password must be at least 8 characters long.")
                sys.exit() 
            writer.writerow({'username': employee_username, 'password': employee_password})
            print("Employee added successfully!")
            yn = input("Do you want to add another user? (yes/no): ")
            if yn.lower() == 'no':
                break

if admin_login():
    add_employee()







