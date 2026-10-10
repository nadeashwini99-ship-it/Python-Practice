print("===== SCHOLARSHIP ELIGIBILITY CHECKER =====")

name = input("Enter student name: ")
marks = float(input("Enter percentage: "))
income = float(input("Enter annual family income (₹): "))

print("\n===== ELIGIBILITY RESULT =====")
print("Student Name:", name)
print("Percentage:", marks, "%")
print("Annual Income: ₹", income)

# Sample criteria for this project
if marks < 0 or marks > 100 or income < 0:
    print("Invalid input! Please enter valid details.")

elif marks >= 60 and income <= 250000:
    print("Result: Eligible under the sample criteria!")
    print("You can check scholarships matching your profile.")

else:
    print("Result: Not eligible under these sample criteria.")
    print("Check other scholarship opportunities.")

print("Thank you!")
