inventory = {}

def add_product():
    name = input("Enter product name: ").strip().title()

    if not name:
        print("Product name cannot be empty!")
        return

    try:
        price = float(input("Enter price (₹): "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative!")
            return

        if name in inventory:
            inventory[name]["quantity"] += quantity
            inventory[name]["price"] = price
        else:
            inventory[name] = {
                "price": price,
                "quantity": quantity
            }

        print("Product saved successfully!")

    except ValueError:
        print("Enter a valid price and whole-number quantity.")


def view_inventory():
    if not inventory:
        print("Inventory is empty!")
        return

    print("\n===== INVENTORY =====")
    total_value = 0

    for name, details in inventory.items():
        price = details["price"]
        quantity = details["quantity"]
        value = price * quantity
        total_value += value

        print(f"{name}: ₹{price:.2f} x {quantity} = ₹{value:.2f}")

    print("---------------------")
    print(f"Total Stock Value: ₹{total_value:.2f}")


def search_product():
    name = input("Enter product to search: ").strip().title()

    if name in inventory:
        details = inventory[name]
        print("Product:", name)
        print("Price: ₹", details["price"])
        print("Quantity:", details["quantity"])
    else:
        print("Product not found!")


while True:
    print("\n===== INVENTORY MANAGER =====")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Search Product")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        search_product()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
