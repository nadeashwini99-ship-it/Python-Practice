print("===== EMPLOYEE SALARY CALCULATOR =====")

name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10
bonus = basic_salary * 0.05

gross_salary = basic_salary + hra + da + bonus

tax = gross_salary * 0.05
net_salary = gross_salary - tax

print("\n===== SALARY DETAILS =====")
print("Employee Name:", name)
print("Basic Salary: ₹", basic_salary)
print("HRA: ₹", hra)
print("DA: ₹", da)
print("Bonus: ₹", bonus)
print("Gross Salary: ₹", gross_salary)
print("Tax: ₹", tax)
print("Net Salary: ₹", net_salary)
