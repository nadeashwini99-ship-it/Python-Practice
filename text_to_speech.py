
import pyttsx3

def speak_text():
    print("===== TEXT TO SPEECH CONVERTER =====")

    text = input("Enter text to speak: ").strip()

    if not text:
        print("Please enter some text!")
        return

    engine = pyttsx3.init()

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    print("\nSpeaking your text...")

    engine.say(text)
    engine.runAndWait()

    print("Speech completed!")


while True:
    speak_text()

    choice = input(
        "\nDo you want to continue? (yes/no): "
    ).strip().lower()

    if choice != "yes":
        print("Thank you for using Text-to-Speech!")
        break
