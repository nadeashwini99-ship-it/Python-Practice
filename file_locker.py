from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


def create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)


def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_file():
    filename = input("Enter text file name: ")

    if not os.path.isfile(filename):
        print("File not found!")
        return

    with open(filename, "rb") as file:
        data = file.read()

    fernet = Fernet(load_key())
    encrypted_data = fernet.encrypt(data)

    with open(filename + ".locked", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")


def decrypt_file():
    filename = input("Enter locked file name: ")

    if not os.path.isfile(filename):
        print("File not found!")
        return

    try:
        with open(filename, "rb") as file:
            data = file.read()

        fernet = Fernet(load_key())
        decrypted_data = fernet.decrypt(data)

        output_name = filename.removesuffix(".locked")

        with open(output_name + ".unlocked.txt", "wb") as file:
            file.write(decrypted_data)

        print("File decrypted successfully!")

    except Exception:
        print("Decryption failed! Check the key and file.")


create_key()

while True:
    print("\n===== FILE LOCKER =====")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        encrypt_file()
    elif choice == "2":
        decrypt_file()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
