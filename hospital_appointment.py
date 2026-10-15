appointments = []

def book_appointment():
    print("\n--- Book Appointment ---")

    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    doctor = input("Enter doctor name: ")
    date = input("Enter appointment date (DD-MM-YYYY): ")
    time = input("Enter appointment time: ")

    if not name.strip() or not doctor.strip():
        print("Patient and doctor names are required!")
        return

    if not age.isdigit() or int(age) <= 0:
        print("Please enter a valid age!")
        return

    appointment = {
        "name": name,
        "age": int(age),
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)
    print("Appointment booked successfully!")


def view_appointments():
    print("\n--- Appointment List ---")

    if not appointments:
        print("No appointments found.")
        return

    for i, appointment in enumerate(appointments, start=1):
        print(f"\nAppointment {i}")
        print("Patient:", appointment["name"])
        print("Age:", appointment["age"])
        print("Doctor:", appointment["doctor"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])


while True:
    print("\n===== HOSPITAL APPOINTMENT SYSTEM =====")
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_appointment()
    elif choice == "2":
        view_appointments()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
