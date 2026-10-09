print("===== WEATHER OUTFIT SUGGESTION =====")

temperature = float(input("Enter temperature in Celsius: "))

if temperature < 10:
    print("Weather: Very Cold 🥶")
    print("Suggestion: Wear a warm jacket and sweater.")

elif temperature < 20:
    print("Weather: Cool 🌥️")
    print("Suggestion: Wear a sweater or light jacket.")

elif temperature < 30:
    print("Weather: Pleasant 😊")
    print("Suggestion: Wear comfortable clothes.")

elif temperature < 40:
    print("Weather: Hot ☀️")
    print("Suggestion: Wear cotton clothes and stay hydrated.")

else:
    print("Weather: Extremely Hot 🔥")
    print("Suggestion: Wear light clothes and avoid direct sunlight.")

print("\nStay comfortable and take care!")
