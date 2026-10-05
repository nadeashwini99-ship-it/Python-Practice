print("===== SHOPPING BILL GENERATOR =====")

items = []

while True:
    name = input("\nEnter item name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

    items.append((name, price, quantity, total))


print("\n========== BILL ==========")

grand_total = 0

for item in items:
    name, price, quantity, total = item

    print(name, "-", quantity, "x ₹", price, "= ₹", total)

    grand_total += total

print("--------------------------")
print("Grand Total: ₹", grand_total)
print("==========================")
print("Thank you for shopping!")
