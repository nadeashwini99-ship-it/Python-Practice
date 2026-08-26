import re

print("===== EMAIL VALIDATOR =====")

email = input("Enter your email: ")

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid Email Address ✅")
else:
    print("Invalid Email Address ❌")
