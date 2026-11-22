print("===== BIRTHDAY WISH GENERATOR =====")

name = input("Enter person's name: ")
age = int(input("Enter their age: "))
relation = input("Your relationship (Friend/ Sister/ Brother/ etc.): ")

print("\n===== YOUR BIRTHDAY MESSAGE =====")

print(f"""
Happy Birthday, {name}! 🎂🎉

Wishing you a wonderful {age}th birthday!

You are an amazing {relation.lower()}, 
and I hope your day is filled with happiness,
love, laughter and beautiful memories.

May all your dreams come true!
Have an unforgettable birthday! ❤️
""")

print("Wish generated successfully!")
