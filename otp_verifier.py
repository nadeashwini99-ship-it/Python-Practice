import random

def generate_otp():
    return random.randint(100000, 999999)


print("===== OTP VERIFICATION SYSTEM =====")

otp = generate_otp()

print("Your OTP is:", otp)

user_otp = int(input("Enter OTP: "))

if user_otp == otp:
    print("OTP Verified Successfully!")
    print("Access Granted.")
else:
    print("Invalid OTP!")
    print("Access Denied.")
