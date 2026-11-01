
import json
import os

FILE = "savings_data.json"


def load_goals():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Could not load saved goals.")
    return {}


def save_goals(goals):
    with open(FILE, "w") as f:
        json.dump(goals, f, indent=4)


def add_goal(goals):
    name = input("Enter your savings goal: ").strip()

    if not name:
        print("Goal name cannot be empty!")
        return

    if name in goals:
        print("This goal already exists!")
        return

    try:
        target = float(input("Enter target amount (Rs.): "))

        if target <= 0:
            print("Target must be greater than zero!")
            return

        goals[name] = {
            "target": target,
            "saved": 0.0
        }

        save_goals(goals)
        print("Savings goal created successfully!")

    except ValueError:
        print("Please enter a valid amount!")


def add_savings(goals):
    if not goals:
        print("Create a goal first!")
        return

    show_goals(goals)
    name = input("Enter goal name: ").strip()

    if name not in goals:
        print("Goal not found!")
        return

    try:
        amount = float(input("Enter amount to save (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        goals[name]["saved"] += amount
        save_goals(goals)

        print("Money added successfully!")

        if goals[name]["saved"] >= goals[name]["target"]:
            print("Congratulations! Your target is reached!")

    except ValueError:
        print("Please enter a valid amount!")


def show_goals(goals):
    print("\n===== SAVINGS GOALS =====")

    if not goals:
        print("No savings goals found!")
        return

    for name, details in goals.items():
        target = details["target"]
        saved = details["saved"]
        remaining = max(0, target - saved)
        progress = min(100, saved / target * 100)

        print(f"\nGoal: {name}")
        print(f"Target: Rs. {target:.2f}")
        print(f"Saved: Rs. {saved:.2f}")
        print(f"Remaining: Rs. {remaining:.2f}")
        print(f"Progress: {progress:.1f}%")


def delete_goal(goals):
    name = input("Enter goal name to delete: ").strip()

    if name in goals:
        del goals[name]
        save_goals(goals)
        print("Goal deleted successfully!")
    else:
        print("Goal not found!")


def main():
    goals = load_goals()

    while True:
        print("\n===== SAVINGS TRACKER =====")
        print("1. Create Savings Goal")
        print("2. Add Savings")
        print("3. View Goals")
        print("4. Delete Goal")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_goal(goals)
        elif choice == "2":
            add_savings(goals)
        elif choice == "3":
            show_goals(goals)
        elif choice == "4":
            delete_goal(goals)
        elif choice == "5":
            print("Keep saving. Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
