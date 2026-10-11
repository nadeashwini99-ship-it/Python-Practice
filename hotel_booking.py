print("===== HOTEL ROOM BOOKING SYSTEM =====")

name = input("Enter customer name: ")

print("\nRoom Types:")
print("1. Standard - ₹1000 per night")
print("2. Deluxe   - ₹2000 per night")
print("3. Suite    - ₹3500 per night")

choice = input("\nChoose room type (1-3): ")
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Please enter valid number of nights.")

elif choice == "1":
    room = "Standard"
    price = 1000

elif choice == "2":
    room = "Deluxe"
    price = 2000

elif choice == "3":
    room = "Suite"
    price = 3500

else:
    room = None
    price = 0
    print("Invalid room choice!")

if price > 0 and nights > 0:
    total = price * nights

    print("\n===== BOOKING RECEIPT =====")
    print("Customer:", name)
    print("Room Type:", room)
    print("Number of Nights:", nights)
    print("Price per Night: ₹", price)
    print("Total Bill: ₹", total)
    print("Booking completed successfully!")
