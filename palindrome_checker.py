print("===== PALINDROME CHECKER =====")

text = input("Enter a word or number: ")

clean_text = text.lower().replace(" ", "")

if clean_text == clean_text[::-1]:
    print("It is a Palindrome ✅")
else:
    print("It is not a Palindrome ❌")
