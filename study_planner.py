
import json
import os
from datetime import date

FILE = "study_tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Could not load saved tasks.")
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    subject = input("Enter subject name: ").strip()
    topic = input("Enter topic to study: ").strip()

    if not subject or not topic:
        print("Subject and topic are required!")
        return

    try:
        hours = float(input("Enter study hours: "))

        if hours <= 0:
            print("Hours must be greater than zero!")
            return

        tasks.append({
            "subject": subject,
            "topic": topic,
            "hours": hours,
            "date": str(date.today()),
            "completed": False
        })

        save_tasks(tasks)
        print("Study task added successfully!")

    except ValueError:
        print("Please enter a valid number!")


def view_tasks(tasks):
    print("\n===== YOUR STUDY PLAN =====")

    if not tasks:
        print("No study tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"\n{i}. Subject: {task['subject']}")
        print(f"   Topic: {task['topic']}")
        print(f"   Study hours: {task['hours']}")
        print(f"   Date: {task['date']}")
        print(f"   Status: {status}")


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Great! Study task completed!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Enter a valid number!")


def show_progress(tasks):
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    hours = sum(
        task["hours"] for task in tasks if task["completed"]
    )

    print("\n===== STUDY PROGRESS =====")
    print("Total tasks:", total)
    print("Completed tasks:", completed)
    print("Pending tasks:", total - completed)
    print(f"Completed study hours: {hours:.1f}")

    if total:
        print(f"Progress: {completed / total * 100:.1f}%")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== SMART STUDY PLANNER =====")
        print("1. Add Study Task")
        print("2. View Study Plan")
        print("3. Mark Task Completed")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            show_progress(tasks)
        elif choice == "5":
            print("Keep learning. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
