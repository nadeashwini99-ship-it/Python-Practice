contacts = {}

print("===== CONTACT MANAGER =====")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact saved successfully! ✅")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            print("\n----- Contacts -----")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found! ❌")

    elif choice == "4":
        name = input("Enter name to update: ")

        if name in contacts:
            new_phone = input("Enter new phone number: ")
            contacts[name] = new_phone
            print("Contact updated successfully! ✅")
        else:
            print("Contact not found! ❌")

    elif choice == "5":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully! ✅")
        else:
            print("Contact not found! ❌")

    elif choice == "6":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice! ❌")
