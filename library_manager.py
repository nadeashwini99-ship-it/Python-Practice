
import json
import os

FILE_NAME = "library.json"


def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty!")
        return

    books.append({
        "title": title,
        "author": author,
        "available": True
    })

    save_books(books)
    print("Book added successfully!")


def show_books(books):
    if not books:
        print("No books available.")
        return

    for i, book in enumerate(books, start=1):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{i}. {book['title']} - {book['author']} [{status}]")


def search_book(books):
    keyword = input("Enter book title: ").lower()

    for book in books:
        if keyword in book["title"].lower():
            print(book)
            return

    print("Book not found.")


def borrow_book(books):
    title = input("Enter book title to borrow: ").lower()

    for book in books:
        if book["title"].lower() == title:
            if book["available"]:
                book["available"] = False
                save_books(books)
                print("Book borrowed successfully!")
            else:
                print("This book is already borrowed.")
            return

    print("Book not found.")


def return_book(books):
    title = input("Enter book title to return: ").lower()

    for book in books:
        if book["title"].lower() == title:
            if not book["available"]:
                book["available"] = True
                save_books(books)
                print("Book returned successfully!")
            else:
                print("This book was not borrowed.")
            return

    print("Book not found.")


def main():
    books = load_books()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            show_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            print("Thank you for using Library System!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
