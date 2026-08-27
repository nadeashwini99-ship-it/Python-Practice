print("===== QUIZ SCORE CALCULATOR =====")

total_questions = int(input("Enter total questions: "))
correct_answers = int(input("Enter correct answers: "))

wrong_answers = total_questions - correct_answers
percentage = (correct_answers / total_questions) * 100

print("\n----- Quiz Result -----")
print("Total Questions:", total_questions)
print("Correct Answers:", correct_answers)
print("Wrong Answers:", wrong_answers)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    print("Result: Excellent! 🏆")
elif percentage >= 75:
    print("Result: Very Good! 🎉")
elif percentage >= 50:
    print("Result: Good! 👍")
else:
    print("Result: Keep Practicing! 💪")
