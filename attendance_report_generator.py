
import csv
from datetime import datetime

def generate_attendance():
    students = []

    print("===== STUDENT ATTENDANCE SYSTEM =====")

    while True:
        name = input("\nEnter student name (or 'done'): ")

        if name.lower() == "done":
            break

        roll = input("Enter roll number: ")

        status = input("Present or Absent (P/A): ").upper()

        if status not in ["P", "A"]:
            print("Invalid status! Enter P or A.")
            continue

        students.append({
            "Roll Number": roll,
            "Name": name,
            "Status": "Present" if status == "P" else "Absent"
        })

    if not students:
        print("No attendance records found.")
        return

    filename = "attendance_report.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        fields = ["Roll Number", "Name", "Status"]
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(students)

    present = sum(1 for s in students if s["Status"] == "Present")
    absent = len(students) - present

    print("\n===== ATTENDANCE REPORT =====")
    print("Total Students:", len(students))
    print("Present:", present)
    print("Absent:", absent)
    print("Attendance Percentage:", round(present / len(students) * 100, 2), "%")
    print("\nReport saved as", filename)


generate_attendance()
