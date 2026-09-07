print("===== BILL SPLITTER =====")

bill = float(input("Enter total bill amount: ₹"))
people = int(input("Enter number of people: "))

if bill > 0 and people > 0:
    per_person = bill / people

    print("\n===== BILL DETAILS =====")
    print("Total Bill: ₹", round(bill, 2))
    print("Number of People:", people)
    print("Each Person Pays: ₹", round(per_person, 2))
else:
    print("Please enter valid values! ❌")
