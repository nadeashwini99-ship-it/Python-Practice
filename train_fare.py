print("===== TRAIN FARE CALCULATOR =====")

name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))
distance = float(input("Enter travel distance (km): "))

print("\nTicket Category:")
print("1. General")
print("2. AC")

choice = input("Choose category (1 or 2): ")

if age < 0 or distance <= 0:
    print("Invalid age or distance!")

elif choice not in ("1", "2"):
    print("Invalid ticket category!")

else:
    if choice == "1":
        rate = 1.5
        category = "General"
    else:
        rate = 3.0
        category = "AC"

    fare = distance * rate

    if age < 5:
        fare = 0
    elif age >= 60:
        fare *= 0.8

    print("\n===== TICKET DETAILS =====")
    print("Passenger:", name)
    print("Age:", age)
    print("Distance:", distance, "km")
    print("Category:", category)
    print("Total Fare: ₹", round(fare, 2))
    print("Have a safe journey!")
