print("===== CHARACTER FREQUENCY ANALYZER =====")

text = input("Enter a text: ")

frequency = {}

for char in text:
    if char == " ":
        continue

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\nCharacter Frequency:")

for char, count in frequency.items():
    print(char, "->", count)
