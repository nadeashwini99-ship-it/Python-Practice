print("===== STUDENT MARKS ANALYZER =====")

marks = []

number = int(input("How many subjects? "))

for i in range(number):
    mark = float(input(f"Enter marks for subject {i + 1}: "))

    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print("Invalid marks! Enter between 0 and 100.")
        break

if len(marks) == number:
    total = sum(marks)
    average = total / number
    highest = max(marks)
    lowest = min(marks)

    print("\n===== RESULT =====")
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

    if average >= 75:
        print("Performance: Excellent 🏆")
    elif average >= 60:
        print("Performance: Very Good 🎉")
    elif average >= 50:
        print("Performance: Good 👍")
    else:
        print("Performance: Need Improvement 💪")
