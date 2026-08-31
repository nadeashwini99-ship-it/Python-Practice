candidates = {
    "1": {"name": "Candidate A", "votes": 0},
    "2": {"name": "Candidate B", "votes": 0},
    "3": {"name": "Candidate C", "votes": 0}
}

print("===== SIMPLE VOTING SYSTEM =====")

voters = set()

while True:
    print("\n1. Vote")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        voter_id = input("Enter your voter ID: ")

        if voter_id in voters:
            print("You have already voted! ❌")
            continue

        print("\nCandidates:")
        for number, candidate in candidates.items():
            print(number + ".", candidate["name"])

        vote = input("Enter candidate number: ")

        if vote in candidates:
            candidates[vote]["votes"] += 1
            voters.add(voter_id)
            print("Vote recorded successfully! ✅")
        else:
            print("Invalid candidate! ❌")

    elif choice == "2":
        print("\n===== VOTING RESULTS =====")

        for candidate in candidates.values():
            print(candidate["name"], ":", candidate["votes"], "votes")

    elif choice == "3":
        print("Thank you for using the Voting System! 👋")
        break

    else:
        print("Invalid choice! ❌")
