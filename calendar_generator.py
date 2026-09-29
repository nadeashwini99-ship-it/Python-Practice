import calendar

print("===== CALENDAR GENERATOR =====")

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

if 1 <= month <= 12:
    print("\n")
    print(calendar.month(year, month))
else:
    print("Invalid month! Please enter a number between 1 and 12.")
