# ATM Simulator

balance = 10000
pin = 1234

print("===== WELCOME TO ATM =====")

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"💰 Available Balance: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))

            if amount > 0:
                balance += amount
                print(f"✅ ₹{amount} deposited successfully.")
                print(f"New Balance: ₹{balance}")
            else:
                print("❌ Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("❌ Invalid amount.")
            elif amount > balance:
                print("❌ Insufficient balance.")
            else:
                balance -= amount
                print(f"✅ Please collect your cash: ₹{amount}")
                print(f"Remaining Balance: ₹{balance}")

        elif choice == "4":
            print("Thank you for using ATM! 👋")
            break

        else:
            print("❌ Invalid choice.")

else:
    print("❌ Incorrect PIN!")
    print("Transaction cancelled.")
