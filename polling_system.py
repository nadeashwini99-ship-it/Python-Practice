print("===== ANONYMOUS POLLING SYSTEM =====")

options = {
    "1": "Python",
    "2": "Java",
    "3": "C++",
    "4": "JavaScript"
}

votes = {option: 0 for option in options.values()}
voters = set()

while True:
    print("\n----- MENU -----")
    print("1. Cast Vote")
    print("2. View Results")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        voter_id = input("Enter your voter ID: ").strip()

        if not voter_id:
            print("Voter ID cannot be empty.")

        elif voter_id in voters:
            print("You have already voted!")

        else:
            print("\nChoose your favourite language:")

            for key, language in options.items():
                print(f"{key}. {language}")

            vote = input("Enter your choice: ")

            if vote in options:
                votes[options[vote]] += 1
                voters.add(voter_id)
                print("Vote recorded successfully!")
            else:
                print("Invalid choice. Vote not recorded.")

    elif choice == "2":
        print("\n===== POLL RESULTS =====")

        total_votes = sum(votes.values())

        for language, count in votes.items():
            print(f"{language}: {count} votes")

        print("Total votes:", total_votes)

    elif choice == "3":
        print("Thank you for participating!")
        break

    else:
        print("Invalid option. Try again.")
