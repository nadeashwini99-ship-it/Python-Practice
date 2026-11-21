books = {}

def add_book():
    name = input("Enter book name: ").strip()

    if not name:
        print("Book name cannot be empty!")
        return

    try:
        pages = int(input("Enter total pages: "))

        if pages <= 0:
            print("Pages must be greater than zero!")
            return

        books[name] = {
            "total_pages": pages,
            "read_pages": 0
        }

        print("Book added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def update_progress():
    name = input("Enter book name: ")

    if name not in books:
        print("Book not found!")
        return

    try:
        read = int(input("Enter pages read so far: "))

        total = books[name]["total_pages"]

        if read < 0 or read > total:
            print("Invalid page count!")
            return

        books[name]["read_pages"] = read

        percentage = (read / total) * 100

        print("Progress:", round(percentage, 2), "%")

        if read == total:
            print("Congratulations! Book completed! 🎉")

    except ValueError:
        print("Enter a valid number.")


def view_books():
    if not books:
        print("No books added yet!")
        return

    print("\n===== READING LIST =====")

    for name, details in books.items():
        total = details["total_pages"]
        read = details["read_pages"]
        percentage = (read / total) * 100

        print(f"\nBook: {name}")
        print(f"Pages: {read}/{total}")
        print(f"Progress: {percentage:.1f}%")


while True:
    print("\n===== BOOK READING TRACKER =====")
    print("1. Add Book")
    print("2. Update Reading Progress")
    print("3. View Books")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        update_progress()

    elif choice == "3":
        view_books()

    elif choice == "4":
        print("Happy Reading! 📚")
        break

    else:
        print("Invalid choice!")
