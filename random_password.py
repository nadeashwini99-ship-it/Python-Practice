import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)
    print("Password length:", len(password))
