import json
from difflib import get_close_matches

dictionary = {
    "apple": "A sweet fruit that grows on trees.",
    "python": "A popular programming language.",
    "computer": "An electronic device used for processing data.",
    "beautiful": "Pleasing to the senses or mind.",
    "happy": "Feeling joy or pleasure.",
    "book": "A collection of written or printed pages.",
    "education": "The process of learning and gaining knowledge.",
    "friend": "A person you know and trust."
}

print("===== ENGLISH DICTIONARY =====")

while True:
    print("\n1. Search Word")
    print("2. Add New Word")
    print("3. View All Words")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter a word: ").lower().strip()

        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            matches = get_close_matches(
                word, dictionary.keys(), n=1, cutoff=0.6
            )

            if matches:
                print("Did you mean:", matches[0])
                print("Meaning:", dictionary[matches[0]])
            else:
                print("Word not found!")

    elif choice == "2":
        word = input("Enter new word: ").lower().strip()
        meaning = input("Enter meaning: ")

        if word:
            dictionary[word] = meaning
            print("Word added successfully!")

    elif choice == "3":
        for word, meaning in sorted(dictionary.items()):
            print(f"{word}: {meaning}")

    elif choice == "4":
        print("Thank you for using Dictionary App!")
        break

    else:
        print("Invalid choice!")
