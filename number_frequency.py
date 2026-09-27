print("===== NUMBER FREQUENCY COUNTER =====")

numbers = input("Enter numbers separated by spaces: ")

numbers = numbers.split()

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("\nNumber Frequency:")

for number, count in frequency.items():
    print(number, "->", count)
