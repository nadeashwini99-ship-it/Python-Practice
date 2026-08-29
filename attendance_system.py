students = {}

print("===== STUDENT ATTENDANCE SYSTEM =====")

while True:
    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name not in students:
            students[name] = 0
            print("Student added successfully! ✅")
        else:
            print("Student already exists!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            students[name] += 1
            print("Attendance marked successfully! ✅")
        else:
            print("Student not found! ❌")

    elif choice == "3":
        if not students:
            print("No students available.")
        else:
            print("\n----- Attendance -----")

            for name, attendance in students.items():
                print(f"{name}: {attendance} days")

    elif choice == "4":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice! ❌")
