print("===== GCD & LCM CALCULATOR =====")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a = num1
b = num2

# Find GCD
while b != 0:
    a, b = b, a % b

gcd = a

# Find LCM
if num1 == 0 or num2 == 0:
    lcm = 0
else:
    lcm = abs(num1 * num2) // gcd

print("\n----- Result -----")
print("GCD:", gcd)
print("LCM:", lcm)
