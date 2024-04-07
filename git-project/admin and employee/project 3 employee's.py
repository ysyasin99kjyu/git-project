import datetime
import csv
import os

def login():
    with open('employees.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        username = input("Enter your username (employee): ")
        password = input("Enter your password (employee): ")
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return username
    return None

def record_attendance(username):
    current_time = datetime.datetime.now()
    attendance_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open("attendance_records.txt", "a") as file:
        file.write(f"Employee: {username} - Attendance Time: {attendance_time}\n")
    print("Attendance recorded successfully.")

def main():
    user = login()
    if user:
        record_attendance(user)
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()