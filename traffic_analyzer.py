print("===== WEBSITE TRAFFIC ANALYZER =====")

visitors = []

days = int(input("Enter number of days to analyze: "))

if days <= 0:
    print("Please enter a valid number of days.")

else:
    for day in range(1, days + 1):
        while True:
            try:
                count = int(
                    input(f"Enter visitors on day {day}: ")
                )

                if count < 0:
                    print("Visitors cannot be negative!")
                    continue

                visitors.append(count)
                break

            except ValueError:
                print("Please enter a whole number.")

    total = sum(visitors)
    average = total / days
    highest = max(visitors)
    lowest = min(visitors)

    print("\n===== TRAFFIC REPORT =====")
    print("Total Visitors:", total)
    print("Average Visitors:", round(average, 2))
    print("Highest Visitors:", highest)
    print("Lowest Visitors:", lowest)

    busiest_day = visitors.index(highest) + 1
    print("Busiest Day:", busiest_day)

    print("\nDaily Visitor Details:")
    for day, count in enumerate(visitors, start=1):
        print(f"Day {day}: {count} visitors")

    print("\nAnalysis completed successfully!")
