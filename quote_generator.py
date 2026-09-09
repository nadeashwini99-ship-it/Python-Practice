import random

quotes = [
    "Believe in yourself.",
    "Never give up.",
    "Dream big and work hard.",
    "Every day is a new beginning.",
    "Success comes from consistent effort.",
    "Your future depends on what you do today.",
    "Learn from yesterday and grow today."
]

print("===== RANDOM QUOTE GENERATOR =====")

while True:
    print("\n1. Generate Quote")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        quote = random.choice(quotes)
        print("\n💡 Quote:", quote)

    elif choice == "2":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice! ❌")
