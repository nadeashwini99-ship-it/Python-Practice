
import json
import os

FILE_NAME = "medicine_stock.json"


def load_medicines():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_medicines(medicines):
    with open(FILE_NAME, "w") as file:
        json.dump(medicines, file, indent=4)


def add_medicine(medicines):
    name = input("Enter medicine name: ").strip()
    code = input("Enter medicine code: ").strip().upper()

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity < 0:
            print("Enter valid price and quantity!")
            return
    except ValueError:
        print("Invalid price or quantity!")
        return

    if not name or not code:
        print("Name and code are required!")
        return

    if any(m["code"] == code for m in medicines):
        print("Medicine code already exists!")
        return

    medicines.append({
        "name": name,
        "code": code,
        "price": price,
        "quantity": quantity
    })

    save_medicines(medicines)
    print("Medicine added successfully!")


def view_medicines(medicines):
    if not medicines:
        print("No medicines available.")
        return

    print("\n===== MEDICINE STOCK =====")

    for medicine in medicines:
        print(f"\nName: {medicine['name']}")
        print(f"Code: {medicine['code']}")
        print(f"Price: Rs. {medicine['price']:.2f}")
        print(f"Stock: {medicine['quantity']}")


def search_medicine(medicines):
    keyword = input("Enter medicine name or code: ").strip().lower()

    for medicine in medicines:
        if (keyword == medicine["code"].lower()
                or keyword in medicine["name"].lower()):
            print("\nMedicine Found!")
            print("Name:", medicine["name"])
            print("Code:", medicine["code"])
            print("Price: Rs.", medicine["price"])
            print("Stock:", medicine["quantity"])
            return

    print("Medicine not found.")


def sell_medicine(medicines):
    code = input("Enter medicine code: ").strip().upper()

    for medicine in medicines:
        if medicine["code"] == code:
            try:
                quantity = int(input("Enter quantity to sell: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    return

                if quantity > medicine["quantity"]:
                    print("Insufficient stock!")
                    return

                medicine["quantity"] -= quantity
                total = quantity * medicine["price"]

                save_medicines(medicines)

                print("\n===== SALES BILL =====")
                print("Medicine:", medicine["name"])
                print("Quantity:", quantity)
                print(f"Total Amount: Rs. {total:.2f}")
                print("Stock updated successfully!")
                return

            except ValueError:
                print("Enter a valid quantity!")
                return

    print("Medicine code not found.")


def main():
    medicines = load_medicines()

    while True:
        print("\n===== MEDICAL STORE MANAGEMENT =====")
        print("1. Add Medicine")
        print("2. View Medicine Stock")
        print("3. Search Medicine")
        print("4. Sell Medicine")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_medicine(medicines)
        elif choice == "2":
            view_medicines(medicines)
        elif choice == "3":
            search_medicine(medicines)
        elif choice == "4":
            sell_medicine(medicines)
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
