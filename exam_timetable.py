from datetime import datetime

print("===== EXAM TIMETABLE GENERATOR =====")

timetable = []

while True:
    subject = input("\nEnter subject name (or 'done' to finish): ")

    if subject.lower() == "done":
        break

    date = input("Enter exam date (DD-MM-YYYY): ")
    time = input("Enter exam time: ")

    try:
        exam_date = datetime.strptime(date, "%d-%m-%Y")

        timetable.append({
            "subject": subject,
            "date": exam_date,
            "time": time
        })

        print("Exam added successfully!")

    except ValueError:
        print("Invalid date format! Try again.")

timetable.sort(key=lambda x: x["date"])

print("\n===== YOUR EXAM TIMETABLE =====")

if not timetable:
    print("No exams added.")

else:
    for index, exam in enumerate(timetable, start=1):
        print(f"\nExam {index}")
        print("Subject:", exam["subject"])
        print("Date:", exam["date"].strftime("%d-%m-%Y"))
        print("Time:", exam["time"])

print("\nBest of luck for your exams! 🎓")
