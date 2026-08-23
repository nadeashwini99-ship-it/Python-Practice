print("===== TEMPERATURE CONVERTER =====")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("Enter your choice: ")
temperature = float(input("Enter temperature: "))

if choice == "1":
    result = (temperature * 9 / 5) + 32
    print("Fahrenheit:", round(result, 2))

elif choice == "2":
    result = (temperature - 32) * 5 / 9
    print("Celsius:", round(result, 2))

elif choice == "3":
    result = temperature + 273.15
    print("Kelvin:", round(result, 2))

elif choice == "4":
    result = temperature - 273.15
    print("Celsius:", round(result, 2))

else:
    print("Invalid choice!")
