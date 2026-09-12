from datetime import datetime

print("===== BIRTHDAY COUNTDOWN =====")

name = input("Enter your name: ")

birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day: "))

today = datetime.now()
year = today.year

birthday = datetime(year, birth_month, birth_day)

if birthday < today:
    birthday = datetime(year + 1, birth_month, birth_day)

days_left = (birthday - today).days

print("\n===== RESULT =====")
print("Name:", name)
print("Days until your next birthday:", days_left)

if days_left == 0:
    print("🎉 Happy Birthday!")
else:
    print("Keep waiting! 🎂")
