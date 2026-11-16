
import json
import os

FILE_NAME = "hostel_data.json"
TOTAL_ROOMS = 10


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


def allocate_room(data):
    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()
    course = input("Enter course name: ").strip()

    if not name or not student_id or not course:
        print("All fields are required!")
        return

    if any(s["student_id"] == student_id for s in data):
        print("Student ID already exists!")
        return

    occupied = [s["room"] for s in data]
    available = [
        room for room in range(101, 101 + TOTAL_ROOMS)
        if room not in occupied
    ]

    if not available:
        print("Sorry! No rooms available.")
        return

    room = available[0]

    data.append({
        "student_id": student_id,
        "name": name,
        "course": course,
        "room": room
    })

    save_data(data)
    print(f"Room {room} allocated successfully!")


def view_students(data):
    if not data:
        print("No students registered.")
        return

    print("\n===== HOSTEL STUDENT DETAILS =====")

    for student in data:
        print("\nStudent ID:", student["student_id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Room:", student["room"])


def search_student(data):
    student_id = input("Enter student ID: ").strip()

    for student in data:
        if student["student_id"] == student_id:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Room:", student["room"])
            return

    print("Student not found.")


def vacate_room(data):
    student_id = input("Enter student ID: ").strip()

    for student in data:
        if student["student_id"] == student_id:
            data.remove(student)
            save_data(data)
            print("Room vacated successfully!")
            return

    print("Student not found.")


def available_rooms(data):
    occupied = [s["room"] for s in data]
    available = [
        room for room in range(101, 101 + TOTAL_ROOMS)
        if room not in occupied
    ]

    print("\nAvailable Rooms:", available)
    print("Total Available:", len(available))


def main():
    data = load_data()

    while True:
        print("\n===== HOSTEL MANAGEMENT SYSTEM =====")
        print("1. Allocate Room")
        print("2. View Students")
        print("3. Search Student")
        print("4. Vacate Room")
        print("5. Check Available Rooms")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            allocate_room(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            vacate_room(data)
        elif choice == "5":
            available_rooms(data)
        elif choice == "6":
            print("Thank you for using Hostel Management System!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
