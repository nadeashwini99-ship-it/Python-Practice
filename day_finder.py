import datetime

print("===== DAY FINDER =====")

date_input = input("Enter date (DD-MM-YYYY): ")

try:
    date = datetime.datetime.strptime(date_input, "%d-%m-%Y")

    print("\nDate:", date.strftime("%d-%m-%Y"))
    print("Day:", date.strftime("%A"))

except ValueError:
    print("Invalid date! Please enter date in DD-MM-YYYY format.")
