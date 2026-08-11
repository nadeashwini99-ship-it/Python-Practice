name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Student Result -----")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
