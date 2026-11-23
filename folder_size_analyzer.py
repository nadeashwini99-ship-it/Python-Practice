import os

print("===== FOLDER SIZE ANALYZER =====")

folder_path = input("Enter folder path: ").strip().strip('"')

if not os.path.isdir(folder_path):
    print("Invalid folder path!")

else:
    total_size = 0
    file_count = 0

    print("\n===== FILE DETAILS =====")

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                size = os.path.getsize(file_path)
                total_size += size
                file_count += 1

                size_kb = size / 1024

                print(f"{filename} - {size_kb:.2f} KB")

            except OSError:
                print("Unable to access:", filename)

    total_mb = total_size / (1024 * 1024)

    print("\n===== SUMMARY =====")
    print("Total Files:", file_count)
    print(f"Total Folder Size: {total_mb:.2f} MB")

    if total_mb > 100:
        print("This folder uses significant storage space.")
    else:
        print("Folder size is within 100 MB.")
