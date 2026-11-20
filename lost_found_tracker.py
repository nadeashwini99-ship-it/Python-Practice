reports = []

def report_item():
    print("\n1. Lost Item")
    print("2. Found Item")

    choice = input("Choose type: ")

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return

    item = input("Enter item name: ").strip()
    location = input("Enter location: ").strip()
    contact = input("Enter contact details: ").strip()

    if not item or not location or not contact:
        print("All fields are required!")
        return

    report = {
        "type": "Lost" if choice == "1" else "Found",
        "item": item.title(),
        "location": location,
        "contact": contact
    }

    reports.append(report)
    print("Report submitted successfully!")


def view_reports():
    if not reports:
        print("\nNo reports available.")
        return

    print("\n===== ALL REPORTS =====")

    for i, report in enumerate(reports, start=1):
        print(f"\nReport {i}")
        print("Type:", report["type"])
        print("Item:", report["item"])
        print("Location:", report["location"])
        print("Contact:", report["contact"])


def search_item():
    keyword = input("Enter item name to search: ").strip().lower()

    found = False

    for report in reports:
        if keyword in report["item"].lower():
            print("\nItem Found!")
            print("Type:", report["type"])
            print("Item:", report["item"])
            print("Location:", report["location"])
            print("Contact:", report["contact"])
            found = True

    if not found:
        print("No matching item found.")


while True:
    print("\n===== LOST & FOUND TRACKER =====")
    print("1. Report Lost/Found Item")
    print("2. View All Reports")
    print("3. Search Item")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        report_item()
    elif choice == "2":
        view_reports()
    elif choice == "3":
        search_item()
    elif choice == "4":
        print("Thank you for using Lost & Found Tracker!")
        break
    else:
        print("Invalid choice!")
