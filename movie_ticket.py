print("===== MOVIE TICKET BOOKING =====")

movie = input("Enter movie name: ")
tickets = int(input("Enter number of tickets: "))

price = 150
total = tickets * price

print("\n===== BOOKING DETAILS =====")
print("Movie:", movie)
print("Tickets:", tickets)
print("Price per ticket: ₹", price)
print("Total Amount: ₹", total)

confirm = input("\nConfirm booking? (yes/no): ").lower()

if confirm == "yes":
    print("\nBooking Confirmed!")
    print("Enjoy your movie 🎬")
else:
    print("\nBooking Cancelled.")
