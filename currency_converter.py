print("===== CURRENCY CONVERTER =====")

amount = float(input("Enter amount in INR: "))

print("\nChoose currency:")
print("1. USD")
print("2. EUR")
print("3. GBP")
print("4. AED")

choice = input("Enter your choice: ")

if choice == "1":
    result = amount / 87
    currency = "USD"

elif choice == "2":
    result = amount / 101
    currency = "EUR"

elif choice == "3":
    result = amount / 116
    currency = "GBP"

elif choice == "4":
    result = amount / 24
    currency = "AED"

else:
    print("Invalid choice!")
    exit()

print("\n----- Conversion Result -----")
print("INR:", amount)
print(currency + ":", round(result, 2))
