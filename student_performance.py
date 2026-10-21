print("===== STUDENT PERFORMANCE ANALYZER =====")

students = {}

while True:
    print("\n1. Add Student")
    print("2. View Results")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        if name in students:
            print("Student already exists!")
            continue

        try:
            marks = []

            for subject in ["English", "Maths", "Science"]:
                mark = float(input(f"Enter {subject} marks (0-100): "))

                if not 0 <= mark <= 100:
                    print("Marks must be between 0 and 100!")
                    break

                marks.append(mark)

            if len(marks) == 3:
                students[name] = marks
                print("Student added successfully!")

        except ValueError:
            print("Please enter valid numeric marks!")

    elif choice == "2":
        if not students:
            print("No student records available.")
            continue

        print("\n===== STUDENT RESULTS =====")

        for name, marks in students.items():
            total = sum(marks)
            percentage = total / len(marks)

            print("\nName:", name)
            print("Total Marks:", total, "/ 300")
            print("Percentage:", round(percentage, 2), "%")

            if percentage >= 75:
                print("Grade: Distinction")
            elif percentage >= 60:
                print("Grade: First Class")
            elif percentage >= 35:
                print("Grade: Pass")
            else:
                print("Grade: Fail")

    elif choice == "3":
        if not students:
            print("No student records available.")
        else:
            topper = max(
                students,
                key=lambda name: sum(students[name])
            )

            print("\nClass Topper:", topper)
            print("Total Marks:", sum(students[topper]), "/ 300")

    elif choice == "4":
        print("Thank you for using Student Performance Analyzer!")
        break

    else:
        print("Invalid choice! Please try again.")
