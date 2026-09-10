print("===== LOGIN SYSTEM =====")

users = {
    "ashwini": "python123",
    "student": "hello123",
    "admin": "admin123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("\nLogin Successful! ✅")
    print("Welcome,", username)
else:
    print("\nInvalid username or password! ❌")
