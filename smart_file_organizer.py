import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path!")
        return

    organized = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        if not extension:
            category = "Other_Files"
        elif extension in [".jpg", ".jpeg", ".png", ".gif"]:
            category = "Images"
        elif extension in [".pdf", ".docx", ".txt", ".pptx"]:
            category = "Documents"
        elif extension in [".mp3", ".wav"]:
            category = "Audio"
        elif extension in [".mp4", ".mkv"]:
            category = "Videos"
        elif extension in [".py", ".c", ".cpp", ".java"]:
            category = "Code_Files"
        else:
            category = "Other_Files"

        destination = os.path.join(folder_path, category)
        os.makedirs(destination, exist_ok=True)

        new_path = os.path.join(destination, filename)

        if os.path.exists(new_path):
            print("Skipped duplicate name:", filename)
            continue

        try:
            shutil.move(file_path, new_path)
            print(f"Moved: {filename} -> {category}")
            organized += 1
        except OSError as error:
            print(f"Could not move {filename}: {error}")

    print(f"\nOrganization complete! Files moved: {organized}")


print("===== SMART FILE ORGANIZER =====")
folder = input("Enter folder path: ").strip().strip('"')

confirm = input(
    "Files will be moved into subfolders. Continue? (yes/no): "
).strip().lower()

if confirm == "yes":
    organize_files(folder)
else:
    print("Operation cancelled.")
