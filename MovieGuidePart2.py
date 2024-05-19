# Aaron kotz, CIS261, MovieGuidePart2

import os

# Part 1: Create and initialize movies.txt
def initialize_movies_file():
    with open('movies.txt', 'w') as file:
        file.write('Cat on a Hot Tin Roof\n')
        file.write('On the Waterfront\n')
        file.write('Monty Python and the Holy Grail\n')

# Part 2: Display heading and menu
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

# Part 3: Read movies from file into a list
def read_movies():
    if not os.path.exists('movies.txt'):
        initialize_movies_file()

    with open('movies.txt', 'r') as file:
        movies = [line.strip() for line in file]
    return movies

# Function to write movies list back to file
def write_movies(movies):
    with open('movies.txt', 'w') as file:
        for movie in movies:
            file.write(f"{movie}\n")

# Part 4: Define functions for each command
def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()

def add_movie(movies):
    movie = input("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(f"{movie} was added.\n")

def delete_movie(movies):
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movies):
            removed_movie = movies.pop(number - 1)
            write_movies(movies)
            print(f"{removed_movie} was deleted.\n")
        else:
            print("Invalid movie number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def main():
    initialize_movies_file()
    movies = read_movies()
    display_menu()

    while True:
        command = input("Command: ").strip().lower()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
            list_movies(movies)
        elif command == "del":
            delete_movie(movies)
            list_movies(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()
