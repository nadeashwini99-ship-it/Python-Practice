
import difflib
import os

def compare_files():
    file1 = input("Enter first file path: ").strip()
    file2 = input("Enter second file path: ").strip()

    try:
        with open(file1, "r", encoding="utf-8") as f:
            text1 = f.readlines()

        with open(file2, "r", encoding="utf-8") as f:
            text2 = f.readlines()

        differences = list(difflib.unified_diff(
            text1,
            text2,
            fromfile="First File",
            tofile="Second File"
        ))

        if differences:
            print("\nDifferences found:\n")
            print("".join(differences))
        else:
            print("\nBoth files are identical!")

        output_file = "comparison_result.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            if differences:
                f.writelines(differences)
            else:
                f.write("Both files are identical!")

        print("\nResult saved in:", os.path.abspath(output_file))

    except FileNotFoundError:
        print("Error: File not found!")

    except Exception as error:
        print("Error:", error)


compare_files()
