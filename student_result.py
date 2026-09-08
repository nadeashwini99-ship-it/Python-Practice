print("===== STUDENT RESULT SYSTEM =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))

total = maths + science + english + computer
percentage = total / 4

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 400")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

if percentage >= 50:
    print("Result: PASS ✅")
else:
    print("Result: FAIL ❌")
