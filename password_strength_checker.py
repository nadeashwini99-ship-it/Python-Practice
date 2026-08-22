password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1
if any(i.isupper() for i in password):
    strength += 1
if any(i.islower() for i in password):
    strength += 1
if any(i.isdigit() for i in password):
    strength += 1
if any(i in "@#$%&*!" for i in password):
    strength += 1

if strength == 5:
    print("Strong Password")
elif strength >= 3:
    print("Medium Password")
else:
    print("Weak Password")
