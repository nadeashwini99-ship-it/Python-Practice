
students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    try:
        total_fee = float(input("Enter Total Fees: "))
        paid_fee = float(input("Enter Paid Fees: "))

        if total_fee < 0 or paid_fee < 0 or paid_fee > total_fee:
            print("Invalid fee amount!")
            return

        students[roll] = {
            "name": name,
            "total": total_fee,
            "paid": paid_fee
        }

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numbers!")

def pay_fee():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    try:
        amount = float(input("Enter payment amount: "))

        if amount <= 0:
            print("Enter a valid amount!")
            return

        remaining = students[roll]["total"] - students[roll]["paid"]

        if amount > remaining:
            print("Amount is greater than remaining fees!")
            return

        students[roll]["paid"] += amount
        print("Payment successful!")

    except ValueError:
        print("Invalid amount!")

def show_report():
    if not students:
        print("No student records found!")
        return

    for roll, data in students.items():
        remaining = data["total"] - data["paid"]

        print("\n----------------------")
        print("Roll Number:", roll)
        print("Name:", data["name"])
        print("Total Fees:", data["total"])
        print("Paid Fees:", data["paid"])
        print("Remaining Fees:", remaining)

def main():
    while True:
        print("\n===== FEE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Pay Fees")
        print("3. Show Fee Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            pay_fee()
        elif choice == "3":
            show_report()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

main()
