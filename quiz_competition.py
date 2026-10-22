import random

questions = [
    {
        "question": "Which language is used for AI?",
        "options": ["1. HTML", "2. Python", "3. CSS", "4. XML"],
        "answer": "2"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "1. Central Processing Unit",
            "2. Computer Personal Unit",
            "3. Central Program Utility",
            "4. Control Processing User"
        ],
        "answer": "1"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["1. String", "2. Integer", "3. Boolean", "4. List"],
        "answer": "3"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["1. //", "2. #", "3. <!--", "4. **"],
        "answer": "2"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["1. input()", "2. scan()", "3. print()", "4. show()"],
        "answer": "3"
    }
]

random.shuffle(questions)

score = 0

print("=" * 35)
print("     PYTHON QUIZ COMPETITION")
print("=" * 35)

name = input("Enter your name: ").strip()

if not name:
    name = "Player"

for number, question in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {question['question']}")

    for option in question["options"]:
        print(option)

    answer = input("Enter your answer (1-4): ").strip()

    if answer == question["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")
        print("Correct option:", question["answer"])

print("\n" + "=" * 35)
print("         QUIZ RESULT")
print("=" * 35)

percentage = (score / len(questions)) * 100

print("Player:", name)
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)
print("Score:", f"{percentage:.1f}%")

if percentage == 100:
    print("Excellent! Perfect score!")
elif percentage >= 60:
    print("Great job! Keep learning!")
else:
    print("Keep practicing. You can do it!")

print("=" * 35)
