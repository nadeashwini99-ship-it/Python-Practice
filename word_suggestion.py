from difflib import get_close_matches

print("===== WORD SUGGESTION SYSTEM =====")

words = [
    "apple", "banana", "computer", "python",
    "programming", "developer", "keyboard",
    "education", "internet", "software",
    "student", "college", "technology",
    "science", "language", "project"
]

while True:
    user_word = input(
        "\nEnter a word (or type 'exit' to quit): "
    ).strip().lower()

    if user_word == "exit":
        print("Thank you for using Word Suggestion System!")
        break

    if not user_word:
        print("Please enter a word.")
        continue

    if user_word in words:
        print("Correct! Word found:", user_word)
    else:
        suggestions = get_close_matches(
            user_word, words, n=3, cutoff=0.5
        )

        if suggestions:
            print("Did you mean:")
            for index, word in enumerate(suggestions, start=1):
                print(f"{index}. {word}")
        else:
            print("No suggestions found. Try another word.")
