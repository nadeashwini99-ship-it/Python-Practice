score = 0

print("===== Python Quiz Game =====")

questions = [
    ("What is the full form of CPU?", "central processing unit"),
    ("Which language is used for web pages?", "html"),
    ("What is the extension of a Python file?", ".py"),
    ("Which symbol is used for comments in Python?", "#"),
    ("Which keyword is used to define a function in Python?", "def")
]

for question, answer in questions:
    print("\n" + question)
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == answer:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")
        print("Correct answer:", answer)

print("\n===== Quiz Result =====")
print("Your Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! 🎉")
elif score >= 3:
    print("Good job! 👍")
else:
    print("Keep practicing! 💪")
