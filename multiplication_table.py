print("===== MULTIPLICATION TABLE GENERATOR =====")

while True:
    print("\n1. Generate Table")
    print("2. Generate Tables in Range")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number = int(input("Enter a number: "))
        limit = int(input("Enter table limit: "))

        print(f"\nTable of {number}")

        for i in range(1, limit + 1):
            print(f"{number} x {i} = {number * i}")

    elif choice == "2":
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        for number in range(start, end + 1):
            print(f"\nTable of {number}")

            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")

    elif choice == "3":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice! Try again.")
