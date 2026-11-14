
import json
import os
from datetime import datetime, timedelta

FILE_NAME = "bus_passes.json"


def load_passes():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_passes(passes):
    with open(FILE_NAME, "w") as file:
        json.dump(passes, file, indent=4)


def create_pass(passes):
    name = input("Enter passenger name: ").strip()
    age = input("Enter age: ").strip()
    route = input("Enter bus route: ").strip()

    if not name or not age.isdigit() or not route:
        print("Please enter valid details!")
        return

    pass_id = "BP" + str(int(datetime.now().timestamp()))

    new_pass = {
        "pass_id": pass_id,
        "name": name,
        "age": int(age),
        "route": route,
        "issue_date": datetime.now().strftime("%d-%m-%Y"),
        "expiry_date": (
            datetime.now() + timedelta(days=30)
        ).strftime("%d-%m-%Y")
    }

    passes.append(new_pass)
    save_passes(passes)

    print("\nBus pass created successfully!")
    print("Your Pass ID:", pass_id)


def view_passes(passes):
    if not passes:
        print("No bus passes available.")
        return

    for bus_pass in passes:
        print("\n-------------------------")
        for key, value in bus_pass.items():
            print(f"{key.replace('_', ' ').title()}: {value}")


def search_pass(passes):
    pass_id = input("Enter Pass ID: ").strip().upper()

    for bus_pass in passes:
        if bus_pass["pass_id"].upper() == pass_id:
            print("\nPass Found!")
            for key, value in bus_pass.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            return

    print("Pass not found.")


def delete_pass(passes):
    pass_id = input("Enter Pass ID to delete: ").strip().upper()

    for bus_pass in passes:
        if bus_pass["pass_id"].upper() == pass_id:
            passes.remove(bus_pass)
            save_passes(passes)
            print("Bus pass deleted successfully!")
            return

    print("Pass not found.")


def main():
    passes = load_passes()

    while True:
        print("\n===== BUS PASS MANAGEMENT =====")
        print("1. Create New Pass")
        print("2. View All Passes")
        print("3. Search Pass")
        print("4. Delete Pass")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_pass(passes)
        elif choice == "2":
            view_passes(passes)
        elif choice == "3":
            search_pass(passes)
        elif choice == "4":
            delete_pass(passes)
        elif choice == "5":
            print("Thank you for using Bus Pass Manager!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
