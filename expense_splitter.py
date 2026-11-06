
def add_expense(expenses):
    name = input("Enter person name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount!")


def show_expenses(expenses):
    print("\n===== EXPENSE DETAILS =====")

    if not expenses:
        print("No expenses recorded!")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['name']} - "
            f"Rs. {expense['amount']:.2f}"
        )


def calculate_split(expenses):
    if not expenses:
        print("Add expenses first!")
        return

    total = sum(item["amount"] for item in expenses)
    people = list(dict.fromkeys(
        item["name"] for item in expenses
    ))

    share = total / len(people)

    paid = {person: 0 for person in people}

    for item in expenses:
        paid[item["name"]] += item["amount"]

    print("\n===== SPLIT SUMMARY =====")
    print(f"Total Expense: Rs. {total:.2f}")
    print(f"Number of People: {len(people)}")
    print(f"Each Person Should Pay: Rs. {share:.2f}")

    for person in people:
        difference = paid[person] - share

        if difference > 0:
            print(f"{person} should receive Rs. {difference:.2f}")
        elif difference < 0:
            print(f"{person} should pay Rs. {-difference:.2f}")
        else:
            print(f"{person} is settled!")


def main():
    expenses = []

    while True:
        print("\n===== EXPENSE SPLITTER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Split")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            calculate_split(expenses)
        elif choice == "4":
            print("Thank you for using Expense Splitter!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
