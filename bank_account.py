balance = 5000

print("===== BANK ACCOUNT SYSTEM =====")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance += amount
            print("Deposit successful! ✅")
            print("Updated Balance: ₹", balance)
        else:
            print("Enter a valid amount! ❌")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Enter a valid amount! ❌")
        elif amount > balance:
            print("Insufficient balance! ❌")
        else:
            balance -= amount
            print("Withdrawal successful! ✅")
            print("Remaining Balance: ₹", balance)

    elif choice == "4":
        print("Thank you for using Bank Account System! 👋")
        break

    else:
        print("Invalid choice! ❌")
