def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    total_amount = principal + interest

    return interest, total_amount


print("===== SIMPLE INTEREST CALCULATOR =====")

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

interest, total = calculate_interest(principal, rate, time)

print("\n----- Result -----")
print("Principal Amount:", principal)
print("Simple Interest:", interest)
print("Total Amount:", total)
