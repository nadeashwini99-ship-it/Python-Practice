
from datetime import datetime

MAX_SLOTS = 5
parking = {}


def show_status():
    print("\n===== PARKING STATUS =====")

    for slot in range(1, MAX_SLOTS + 1):
        if slot in parking:
            print(f"Slot {slot}: {parking[slot]['vehicle']}")
        else:
            print(f"Slot {slot}: Available")

    print(f"\nOccupied: {len(parking)}/{MAX_SLOTS}")
    print(f"Available: {MAX_SLOTS - len(parking)}")


def park_vehicle():
    if len(parking) >= MAX_SLOTS:
        print("Parking is full!")
        return

    vehicle = input("Enter vehicle number: ").strip().upper()

    if not vehicle:
        print("Vehicle number cannot be empty!")
        return

    if any(info["vehicle"] == vehicle for info in parking.values()):
        print("This vehicle is already parked!")
        return

    slot = next(
        (s for s in range(1, MAX_SLOTS + 1) if s not in parking),
        None
    )

    parking[slot] = {
        "vehicle": vehicle,
        "time": datetime.now()
    }

    print(f"Vehicle parked successfully in Slot {slot}!")


def remove_vehicle():
    vehicle = input("Enter vehicle number to remove: ").strip().upper()

    for slot, info in list(parking.items()):
        if info["vehicle"] == vehicle:
            duration = datetime.now() - info["time"]
            minutes = max(1, int(duration.total_seconds() / 60))

            # Demo rate: Rs. 10 per started minute
            fee = minutes * 10

            print(f"Parking duration: {minutes} minute(s)")
            print(f"Parking fee: Rs. {fee}")

            del parking[slot]
            print("Vehicle removed successfully!")
            return

    print("Vehicle not found!")


def main():
    while True:
        print("\n===== PARKING MANAGER =====")
        print("1. Park Vehicle")
        print("2. Remove Vehicle")
        print("3. View Parking Status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            remove_vehicle()
        elif choice == "3":
            show_status()
        elif choice == "4":
            print("Parking system closed!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
