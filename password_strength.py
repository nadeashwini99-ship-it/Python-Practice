import string

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in string.punctuation for char in password):
    score += 1

print("\n===== Password Strength =====")

if score <= 2:
    print("Strength: Weak ❌")
elif score <= 4:
    print("Strength: Medium ⚠️")
else:
    print("Strength: Strong ✅")

print("Score:", score, "/ 5")
