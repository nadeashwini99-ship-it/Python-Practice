import random

def create_board():
    board = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]

    solution = [row[:] for row in board]

    for _ in range(40):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        board[row][col] = 0

    return board, solution


def display_board(board):
    print("\n+-------+-------+-------+")

    for i, row in enumerate(board):
        print("|", end=" ")

        for j, number in enumerate(row):
            print(number if number else ".", end=" ")

            if (j + 1) % 3 == 0:
                print("|", end=" ")

        print()

        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")


def play_game():
    board, solution = create_board()

    while True:
        display_board(board)

        print("\n1. Fill a cell")
        print("2. Check solution")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            try:
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
                number = int(input("Enter number (1-9): "))

                if not (0 <= row < 9 and 0 <= col < 9
                        and 1 <= number <= 9):
                    print("Invalid input!")
                    continue

                if board[row][col] != 0:
                    print("This cell is already filled!")
                    continue

                board[row][col] = number
                print("Number added!")

            except ValueError:
                print("Please enter valid numbers!")

        elif choice == "2":
            if board == solution:
                print("Congratulations! Puzzle solved! 🎉")
                break
            else:
                print("Not solved yet. Keep trying!")

        elif choice == "3":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice!")


play_game()
