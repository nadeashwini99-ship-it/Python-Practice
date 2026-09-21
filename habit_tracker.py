import json
import os

FILE = "habits.json"

def load_habits():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return {}

def save_habits(habits):
    with open(FILE, "w") as file:
        json.dump(habits, file, indent=4)

habits = load_habits()

while True:
    print("\n===== DAILY HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit Complete")
    print("4. Delete Habit")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        habit = input("Enter habit name: ").strip()

        if habit and habit not in habits:
            habits[habit] = 0
            save_habits(habits)
            print("Habit added successfully! ✅")
        else:
            print("Invalid or already existing habit!")

    elif choice == "2":
        if not habits:
            print("No habits added yet.")
        else:
            print("\nYour Habits:")
            for habit, count in habits.items():
                print(f"{habit}: Completed {count} times")

    elif choice == "3":
        habit = input("Enter habit name: ").strip()

        if habit in habits:
            habits[habit] += 1
            save_habits(habits)
            print("Habit marked complete! 🎉")
        else:
            print("Habit not found!")

    elif choice == "4":
        habit = input("Enter habit to delete: ").strip()

        if habit in habits:
            del habits[habit]
            save_habits(habits)
            print("Habit deleted successfully!")
        else:
            print("Habit not found!")

    elif choice == "5":
        print("Keep building good habits! 👋")
        break

    else:
        print("Invalid choice!")
