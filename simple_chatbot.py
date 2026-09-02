print("===== SIMPLE CHATBOT =====")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! 👋 How are you?")

    elif "how are you" in user:
        print("Bot: I'm fine! 😊 What about you?")

    elif "your name" in user:
        print("Bot: My name is PyBot.")

    elif "python" in user:
        print("Bot: Python is a popular programming language. 🐍")

    elif "thank" in user:
        print("Bot: You're welcome! 😊")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
