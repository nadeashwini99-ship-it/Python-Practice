import os
import shutil

folder = input("Enter folder path: ")

if not os.path.exists(folder):
    print("Folder not found! ❌")
    exit()

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()
        moved = False

        for category, extensions in file_types.items():

            if extension in extensions:
                category_folder = os.path.join(folder, category)
                os.makedirs(category_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(category_folder, file)
                )

                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder, "Others")
            os.makedirs(other_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(other_folder, file)
            )

print("Files organized successfully! ✅")
