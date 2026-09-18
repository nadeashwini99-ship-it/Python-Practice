print("===== SECRET MESSAGE TOOL =====")

while True:
    print("\n1. Encode Message")
    print("2. Decode Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter your message: ")

        encoded = ""

        for char in message:
            encoded += chr(ord(char) + 3)

        print("Encoded Message:", encoded)

    elif choice == "2":
        message = input("Enter encoded message: ")

        decoded = ""

        for char in message:
            decoded += chr(ord(char) - 3)

        print("Decoded Message:", decoded)

    elif choice == "3":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice! Try again.")
