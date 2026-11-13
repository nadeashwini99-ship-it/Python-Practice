
import json
import os

FILE_NAME = "leave_data.json"


def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_employee(data):
    name = input("Enter employee name: ").strip()
    employee_id = input("Enter employee ID: ").strip()
    department = input("Enter department: ").strip()

    if not name or not employee_id or not department:
        print("All fields are required!")
        return

    if any(emp["id"] == employee_id for emp in data):
        print("Employee ID already exists!")
        return

    data.append({
        "id": employee_id,
        "name": name,
        "department": department,
        "leaves": []
    })

    save_data(data)
    print("Employee added successfully!")


def view_employees(data):
    if not data:
        print("No employees found.")
        return

    for emp in data:
        print(
            f"\nID: {emp['id']}\n"
            f"Name: {emp['name']}\n"
            f"Department: {emp['department']}"
        )


def find_employee(data):
    emp_id = input("Enter employee ID: ").strip()

    for emp in data:
        if emp["id"] == emp_id:
            return emp

    print("Employee not found.")
    return None


def request_leave(data):
    employee = find_employee(data)

    if employee is None:
        return

    date = input("Enter leave date (DD-MM-YYYY): ").strip()
    reason = input("Enter leave reason: ").strip()

    if not date or not reason:
        print("Date and reason are required!")
        return

    employee["leaves"].append({
        "date": date,
        "reason": reason,
        "status": "Pending"
    })

    save_data(data)
    print("Leave request submitted!")


def view_leave_requests(data):
    found = False

    for emp in data:
        for leave in emp["leaves"]:
            found = True
            print(f"\nEmployee: {emp['name']}")
            print("Date:", leave["date"])
            print("Reason:", leave["reason"])
            print("Status:", leave["status"])

    if not found:
        print("No leave requests available.")


def update_leave_status(data):
    employee = find_employee(data)

    if employee is None:
        return

    if not employee["leaves"]:
        print("No leave requests for this employee.")
        return

    for index, leave in enumerate(employee["leaves"], start=1):
        print(
            f"{index}. {leave['date']} - "
            f"{leave['reason']} - {leave['status']}"
        )

    try:
        number = int(input("Select request number: "))

        if number < 1 or number > len(employee["leaves"]):
            print("Invalid request number.")
            return

        print("1. Approve")
        print("2. Reject")
        choice = input("Enter choice: ")

        if choice == "1":
            employee["leaves"][number - 1]["status"] = "Approved"
        elif choice == "2":
            employee["leaves"][number - 1]["status"] = "Rejected"
        else:
            print("Invalid choice.")
            return

        save_data(data)
        print("Leave status updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


def main():
    data = load_data()

    while True:
        print("\n===== EMPLOYEE LEAVE MANAGEMENT =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Request Leave")
        print("4. View Leave Requests")
        print("5. Approve / Reject Leave")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(data)
        elif choice == "2":
            view_employees(data)
        elif choice == "3":
            request_leave(data)
        elif choice == "4":
            view_leave_requests(data)
        elif choice == "5":
            update_leave_status(data)
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
