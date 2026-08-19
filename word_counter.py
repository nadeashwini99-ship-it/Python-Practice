print("===== WORD & CHARACTER COUNTER =====")

text = input("Enter your text: ")

words = text.split()
word_count = len(words)
character_count = len(text)
character_without_spaces = len(text.replace(" ", ""))

print("\n----- Result -----")
print("Words:", word_count)
print("Characters:", character_count)
print("Characters without spaces:", character_without_spaces)
