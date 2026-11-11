
import json
import os

FILE_NAME = "recipes.json"


def load_recipes():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_recipes(recipes):
    with open(FILE_NAME, "w") as file:
        json.dump(recipes, file, indent=4)


def add_recipe(recipes):
    name = input("Enter recipe name: ").strip()
    category = input("Enter category: ").strip()
    ingredients = input("Enter ingredients (comma separated): ").strip()
    steps = input("Enter cooking steps: ").strip()

    if not name or not ingredients or not steps:
        print("Please fill all required details.")
        return

    recipe = {
        "name": name,
        "category": category,
        "ingredients": ingredients,
        "steps": steps
    }

    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully!")


def view_recipes(recipes):
    if not recipes:
        print("No recipes available.")
        return

    for index, recipe in enumerate(recipes, start=1):
        print(f"\nRecipe {index}: {recipe['name']}")
        print("Category:", recipe["category"])
        print("Ingredients:", recipe["ingredients"])
        print("Steps:", recipe["steps"])


def search_recipe(recipes):
    keyword = input("Enter recipe name or ingredient: ").strip().lower()

    found = False

    for recipe in recipes:
        if (keyword in recipe["name"].lower()
                or keyword in recipe["ingredients"].lower()):
            print("\nRecipe:", recipe["name"])
            print("Category:", recipe["category"])
            print("Ingredients:", recipe["ingredients"])
            print("Steps:", recipe["steps"])
            found = True

    if not found:
        print("Recipe not found.")


def delete_recipe(recipes):
    view_recipes(recipes)

    if not recipes:
        return

    try:
        number = int(input("\nEnter recipe number to delete: "))

        if 1 <= number <= len(recipes):
            removed = recipes.pop(number - 1)
            save_recipes(recipes)
            print(removed["name"], "deleted successfully!")
        else:
            print("Invalid recipe number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    recipes = load_recipes()

    while True:
        print("\n===== RECIPE BOOK MANAGER =====")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. Search Recipe")
        print("4. Delete Recipe")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            view_recipes(recipes)
        elif choice == "3":
            search_recipe(recipes)
        elif choice == "4":
            delete_recipe(recipes)
        elif choice == "5":
            print("Thank you for using Recipe Book Manager!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
