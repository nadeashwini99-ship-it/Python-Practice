
import json
import os

FILE = "job_applications.json"

def load_applications():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Unable to load saved applications.")
    return []


def save_applications(applications):
    with open(FILE, "w") as f:
        json.dump(applications, f, indent=4)


def add_application(applications):
    company = input("Enter company name: ").strip()
    role = input("Enter job role: ").strip()
    location = input("Enter job location: ").strip()

    if not company or not role or not location:
        print("All fields are required!")
        return

    application = {
        "company": company,
        "role": role,
        "location": location,
        "status": "Applied"
    }

    applications.append(application)
    save_applications(applications)

    print("Application added successfully!")


def view_applications(applications):
    print("\n===== JOB APPLICATIONS =====")

    if not applications:
        print("No applications found!")
        return

    for i, app in enumerate(applications, start=1):
        print(f"\nApplication {i}")
        print("Company:", app["company"])
        print("Role:", app["role"])
        print("Location:", app["location"])
        print("Status:", app["status"])


def update_status(applications):
    view_applications(applications)

    if not applications:
        return

    try:
        number = int(input("\nEnter application number: "))

        if not 1 <= number <= len(applications):
            print("Invalid application number!")
            return

        print("1. Applied")
        print("2. Interview")
        print("3. Selected")
        print("4. Rejected")

        choice = input("Choose new status: ")

        statuses = {
            "1": "Applied",
            "2": "Interview",
            "3": "Selected",
            "4": "Rejected"
        }

        if choice in statuses:
            applications[number - 1]["status"] = statuses[choice]
            save_applications(applications)
            print("Status updated successfully!")
        else:
            print("Invalid status!")

    except ValueError:
        print("Enter a valid number!")


def search_company(applications):
    name = input("Enter company name: ").strip().lower()

    results = [
        app for app in applications
        if name in app["company"].lower()
    ]

    if results:
        for app in results:
            print(app)
    else:
        print("Company not found!")


def main():
    applications = load_applications()

    while True:
        print("\n===== JOB TRACKER =====")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Update Application Status")
        print("4. Search Company")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            view_applications(applications)
        elif choice == "3":
            update_status(applications)
        elif choice == "4":
            search_company(applications)
        elif choice == "5":
            print("Good luck with your career!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
