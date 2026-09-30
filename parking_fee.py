print("===== PARKING FEE CALCULATOR =====")

vehicle = input("Enter vehicle type (Car/Bike): ").lower()
hours = float(input("Enter parking hours: "))

if hours <= 0:
    print("Invalid parking hours!")

else:
    if vehicle == "car":
        if hours <= 2:
            fee = 30
        else:
            fee = 30 + (hours - 2) * 20

    elif vehicle == "bike":
        if hours <= 2:
            fee = 20
        else:
            fee = 20 + (hours - 2) * 10

    else:
        print("Invalid vehicle type!")
        fee = 0

    if fee > 0:
        print("\n----- Parking Bill -----")
        print("Vehicle:", vehicle.title())
        print("Hours:", hours)
        print("Parking Fee: ₹", round(fee, 2))
