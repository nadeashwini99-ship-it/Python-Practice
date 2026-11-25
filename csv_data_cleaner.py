
import csv
import os

def clean_csv():
    file_path = input("Enter CSV file path: ").strip()

    try:
        with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            rows = list(reader)

        if not rows:
            print("The CSV file is empty.")
            return

        cleaned_rows = []

        for row in rows:
            cleaned_row = [cell.strip() for cell in row]

            if any(cleaned_row):
                cleaned_rows.append(cleaned_row)

        folder = os.path.dirname(file_path)
        filename = os.path.basename(file_path)
        name, extension = os.path.splitext(filename)

        output_path = os.path.join(
            folder, "cleaned_" + name + extension
        )

        with open(output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(cleaned_rows)

        print("\nCSV file cleaned successfully!")
        print("Original rows:", len(rows))
        print("Cleaned rows:", len(cleaned_rows))
        print("Saved file:", output_path)

    except FileNotFoundError:
        print("Error: File not found!")

    except PermissionError:
        print("Error: Permission denied!")

    except Exception as error:
        print("Something went wrong:", error)


clean_csv()
