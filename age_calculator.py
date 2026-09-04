from datetime import date

print("===== AGE CALCULATOR =====")

name = input("Enter your name: ")

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

today = date.today()

age = today.year - birth_year

if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

print("\n===== RESULT =====")
print("Name:", name)
print("Your Age:", age, "years")

if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")
