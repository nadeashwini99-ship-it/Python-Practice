print("===== ELECTRICITY BILL CALCULATOR =====")

name = input("Enter customer name: ")
units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units! Please enter a positive number.")

else:
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = (100 * 3) + (units - 100) * 5
    elif units <= 300:
        bill = (100 * 3) + (100 * 5) + (units - 200) * 7
    else:
        bill = (100 * 3) + (100 * 5) + (100 * 7) + (units - 300) * 10

    fixed_charge = 50
    total_bill = bill + fixed_charge

    print("\n===== BILL RECEIPT =====")
    print("Customer Name:", name)
    print("Units Consumed:", units)
    print("Energy Charge: ₹", round(bill, 2))
    print("Fixed Charge: ₹", fixed_charge)
    print("Total Bill: ₹", round(total_bill, 2))
