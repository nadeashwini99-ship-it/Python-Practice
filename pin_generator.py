import random

print("===== PIN GENERATOR =====")

length = int(input("Enter PIN length: "))

if length <= 0:
    print("Please enter a valid length.")

else:
    pin = ""

    for i in range(length):
        pin += str(random.randint(0, 9))

    print("Generated PIN:", pin)
