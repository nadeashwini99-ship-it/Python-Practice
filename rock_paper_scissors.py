
import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    print("\n===== ROCK PAPER SCISSORS =====")
    print("First to 5 points wins!")

    while player_score < 5 and computer_score < 5:
        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Choose (1-3) or type exit: ").strip().lower()

        if choice == "exit":
            print("Game ended!")
            break

        options = {
            "1": "rock",
            "2": "paper",
            "3": "scissors"
        }

        if choice not in options:
            print("Invalid choice! Try again.")
            continue

        player = options[choice]
        computer = random.choice(choices)

        print("You chose:", player)
        print("Computer chose:", computer)

        if player == computer:
            print("It's a tie!")
        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: You {player_score} - {computer_score} Computer")

    if player_score == 5:
        print("\nCongratulations! You won the game!")
    elif computer_score == 5:
        print("\nComputer won the game. Try again!")

    print("Final Score:", player_score, "-", computer_score)


play_game()
