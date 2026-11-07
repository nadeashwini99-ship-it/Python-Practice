
movies = [
    {"name": "3 Idiots", "genre": "comedy", "rating": 9.0},
    {"name": "Dangal", "genre": "drama", "rating": 8.5},
    {"name": "Inception", "genre": "sci-fi", "rating": 8.8},
    {"name": "Interstellar", "genre": "sci-fi", "rating": 9.2},
    {"name": "Chhichhore", "genre": "comedy", "rating": 8.3},
    {"name": "Taare Zameen Par", "genre": "drama", "rating": 8.7},
    {"name": "The Conjuring", "genre": "horror", "rating": 7.5},
    {"name": "Bhool Bhulaiyaa", "genre": "horror", "rating": 7.8},
    {"name": "Titanic", "genre": "romance", "rating": 8.0},
    {"name": "Jab We Met", "genre": "romance", "rating": 8.1}
]


def show_all_movies():
    print("\n===== ALL MOVIES =====")

    for movie in movies:
        print(
            f"{movie['name']} | "
            f"{movie['genre'].title()} | "
            f"Rating: {movie['rating']}"
        )


def recommend_movies():
    genre = input(
        "\nEnter your favourite genre: "
    ).strip().lower()

    results = [
        movie for movie in movies
        if movie["genre"] == genre
    ]

    results.sort(
        key=lambda movie: movie["rating"],
        reverse=True
    )

    if results:
        print("\n===== RECOMMENDED MOVIES =====")

        for movie in results:
            print(
                f"{movie['name']} "
                f"- Rating: {movie['rating']}"
            )
    else:
        print("No movies found for this genre!")


def search_movie():
    name = input("Enter movie name: ").strip().lower()

    for movie in movies:
        if name in movie["name"].lower():
            print("\nMovie Found!")
            print("Name:", movie["name"])
            print("Genre:", movie["genre"])
            print("Rating:", movie["rating"])
            return

    print("Movie not found!")


def top_movies():
    print("\n===== TOP RATED MOVIES =====")

    top = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )

    for movie in top[:5]:
        print(
            f"{movie['name']} - "
            f"{movie['rating']}/10"
        )


def main():
    while True:
        print("\n===== MOVIE RECOMMENDER =====")
        print("1. Show All Movies")
        print("2. Recommend by Genre")
        print("3. Search Movie")
        print("4. Top Rated Movies")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_movies()
        elif choice == "2":
            recommend_movies()
        elif choice == "3":
            search_movie()
        elif choice == "4":
            top_movies()
        elif choice == "5":
            print("Happy Movie Watching!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
