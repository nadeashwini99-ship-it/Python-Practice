
import json
import os

FILE = "events.json"


def load_events():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Unable to load event data.")
    return {}


def save_events(events):
    with open(FILE, "w") as f:
        json.dump(events, f, indent=4)


def create_event(events):
    name = input("Enter event name: ").strip()
    date = input("Enter event date: ").strip()
    venue = input("Enter event venue: ").strip()

    if not name or not date or not venue:
        print("All details are required!")
        return

    if name in events:
        print("Event already exists!")
        return

    events[name] = {
        "date": date,
        "venue": venue,
        "participants": []
    }

    save_events(events)
    print("Event created successfully!")


def view_events(events):
    print("\n===== COLLEGE EVENTS =====")

    if not events:
        print("No events available!")
        return

    for name, details in events.items():
        print(f"\nEvent: {name}")
        print(f"Date: {details['date']}")
        print(f"Venue: {details['venue']}")
        print(f"Participants: {len(details['participants'])}")


def register_student(events):
    event_name = input("Enter event name: ").strip()

    if event_name not in events:
        print("Event not found!")
        return

    student = input("Enter student name: ").strip()

    if not student:
        print("Student name cannot be empty!")
        return

    participants = events[event_name]["participants"]

    if student.lower() in [p.lower() for p in participants]:
        print("Student already registered!")
        return

    participants.append(student)
    save_events(events)

    print("Registration successful!")


def show_participants(events):
    event_name = input("Enter event name: ").strip()

    if event_name not in events:
        print("Event not found!")
        return

    participants = events[event_name]["participants"]

    print("\n===== PARTICIPANT LIST =====")

    if not participants:
        print("No participants registered!")
        return

    for number, student in enumerate(participants, start=1):
        print(f"{number}. {student}")


def main():
    events = load_events()

    while True:
        print("\n===== COLLEGE EVENT SYSTEM =====")
        print("1. Create Event")
        print("2. View Events")
        print("3. Register Student")
        print("4. View Participants")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_event(events)
        elif choice == "2":
            view_events(events)
        elif choice == "3":
            register_student(events)
        elif choice == "4":
            show_participants(events)
        elif choice == "5":
            print("Thank you for using Event System!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
