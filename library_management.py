books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully! ✅")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")

    elif choice == "3":
        search = input("Enter book name to search: ")

        if search in books:
            print("Book found! ✅")
        else:
            print("Book not found! ❌")

    elif choice == "4":
        book = input("Enter book name to remove: ")

        if book in books:
            books.remove(book)
            print("Book removed successfully! ✅")
        else:
            print("Book not found! ❌")

    elif choice == "5":
        print("Thank you for using Library Management System! 👋")
        break

    else:
        print("Invalid choice! Please try again.")
