
import json
import os

FILE = "donors.json"

def load_donors():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Unable to load donor data.")
    return []


def save_donors(donors):
    with open(FILE, "w") as f:
        json.dump(donors, f, indent=4)


def add_donor(donors):
    name = input("Enter donor name: ").strip()
    blood = input("Enter blood group: ").strip().upper()
    city = input("Enter city: ").strip()
    phone = input("Enter contact number: ").strip()

    valid_groups = [
        "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"
    ]

    if not all([name, blood, city, phone]):
        print("All fields are required!")
        return

    if blood not in valid_groups:
        print("Invalid blood group!")
        return

    if not phone.isdigit() or len(phone) != 10:
        print("Enter a valid 10-digit phone number!")
        return

    donor = {
        "name": name,
        "blood_group": blood,
        "city": city,
        "phone": phone
    }

    donors.append(donor)
    save_donors(donors)
    print("Donor added successfully!")


def view_donors(donors):
    print("\n===== DONOR LIST =====")

    if not donors:
        print("No donor records found!")
        return

    for i, donor in enumerate(donors, start=1):
        print(f"\nDonor {i}")
        print("Name:", donor["name"])
        print("Blood Group:", donor["blood_group"])
        print("City:", donor["city"])
        print("Phone:", donor["phone"])


def search_donor(donors):
    blood = input("Enter required blood group: ").strip().upper()
    city = input("Enter city: ").strip().lower()

    found = False

    for donor in donors:
        if (
            donor["blood_group"] == blood
            and donor["city"].lower() == city
        ):
            print("\nDonor Found!")
            print("Name:", donor["name"])
            print("Contact:", donor["phone"])
            found = True

    if not found:
        print("No matching donor found!")


def delete_donor(donors):
    name = input("Enter donor name to delete: ").strip().lower()

    for donor in donors:
        if donor["name"].lower() == name:
            donors.remove(donor)
            save_donors(donors)
            print("Donor record deleted!")
            return

    print("Donor not found!")


def main():
    donors = load_donors()

    while True:
        print("\n===== BLOOD DONOR MANAGEMENT =====")
        print("1. Add Donor")
        print("2. View Donors")
        print("3. Search Donor")
        print("4. Delete Donor")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_donor(donors)
        elif choice == "2":
            view_donors(donors)
        elif choice == "3":
            search_donor(donors)
        elif choice == "4":
            delete_donor(donors)
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
