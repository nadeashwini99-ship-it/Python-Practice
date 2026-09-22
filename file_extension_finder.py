import os

print("===== FILE EXTENSION FINDER =====")

file_name = input("Enter file name: ")

if "." in file_name:
    name, extension = os.path.splitext(file_name)

    print("\nFile Name:", name)
    print("Extension:", extension)

    if extension.lower() in [".jpg", ".jpeg", ".png", ".gif"]:
        print("Type: Image 🖼️")

    elif extension.lower() in [".mp3", ".wav"]:
        print("Type: Audio 🎵")

    elif extension.lower() in [".mp4", ".mkv", ".avi"]:
        print("Type: Video 🎬")

    elif extension.lower() in [".pdf", ".docx", ".txt", ".xlsx"]:
        print("Type: Document 📄")

    elif extension.lower() == ".py":
        print("Type: Python Program 🐍")

    else:
        print("Type: Other File 📁")

else:
    print("This file has no extension.")
