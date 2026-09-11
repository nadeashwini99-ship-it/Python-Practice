print("===== TEXT ANALYZER =====")

text = input("Enter a sentence: ")

words = text.split()

vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in text.lower():

    if char in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

    elif char.isdigit():
        digits += 1

    elif char.isspace():
        spaces += 1

print("\n===== ANALYSIS =====")
print("Total Words:", len(words))
print("Total Characters:", len(text))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
