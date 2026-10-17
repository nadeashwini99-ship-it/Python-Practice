import os
import hashlib

def calculate_hash(filepath):
    hasher = hashlib.sha256()

    with open(filepath, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def find_duplicates(folder):
    files_by_hash = {}

    for root, dirs, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root, filename)

            try:
                file_hash = calculate_hash(filepath)

                if file_hash not in files_by_hash:
                    files_by_hash[file_hash] = []

                files_by_hash[file_hash].append(filepath)

            except (OSError, PermissionError):
                print("Could not read:", filepath)

    found = False

    print("\n===== DUPLICATE FILES =====")

    for file_list in files_by_hash.values():
        if len(file_list) > 1:
            found = True
            print("\nDuplicate group:")

            for filepath in file_list:
                print(filepath)

    if not found:
        print("No duplicate files found!")


folder = input("Enter folder path: ").strip().strip('"')

if os.path.isdir(folder):
    find_duplicates(folder)
else:
    print("Invalid folder path!")
