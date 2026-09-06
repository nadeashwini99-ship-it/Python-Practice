import random

print("===== DICE ROLLING SIMULATOR =====")

while True:
    choice = input("\nRoll the dice? (yes/no): ").lower()

    if choice == "yes":
        dice = random.randint(1, 6)
        print("🎲 You rolled:", dice)

    elif choice == "no":
        print("Thank you for playing! 👋")
        break

    else:
        print("Please enter yes or no.")
