
products = {
    "rice":  {"price": 60, "stock": 20},
    "sugar": {"price": 45, "stock": 15},
    "milk":  {"price": 30, "stock": 25},
    "oil":   {"price": 150, "stock": 10},
    "bread": {"price": 40, "stock": 12}
}

cart = []


def show_products():
    print("\n===== AVAILABLE PRODUCTS =====")

    for name, details in products.items():
        print(
            f"{name.title()} - Rs.{details['price']} "
            f"| Stock: {details['stock']}"
        )


def add_to_cart():
    show_products()

    name = input("\nEnter product name: ").lower()

    if name not in products:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive!")
        elif quantity > products[name]["stock"]:
            print("Not enough stock available!")
        else:
            products[name]["stock"] -= quantity
            cart.append({
                "name": name,
                "quantity": quantity,
                "price": products[name]["price"]
            })
            print("Product added to cart!")

    except ValueError:
        print("Enter a valid quantity!")


def view_cart():
    print("\n===== YOUR CART =====")

    if not cart:
        print("Your cart is empty!")
        return

    total = 0

    for item in cart:
        amount = item["quantity"] * item["price"]
        total += amount

        print(
            f"{item['name'].title()} x {item['quantity']} "
            f"= Rs.{amount}"
        )

    print("---------------------")
    print("Total Bill: Rs.", total)


def checkout():
    if not cart:
        print("Your cart is empty!")
        return

    view_cart()
    print("\nThank you for shopping!")

    cart.clear()


def main():
    while True:
        print("\n===== GROCERY STORE =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
