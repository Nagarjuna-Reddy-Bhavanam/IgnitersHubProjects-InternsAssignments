from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def read_file(file_name):
    with open(file_name, 'r') as file:
        string_set = set(file.read().splitlines())
    return string_set

def perform_search(search_word, string_set, top_k):
    similar_strings = process.extract(search_word, string_set, limit=top_k)
    return similar_strings

def main():
    file_name = "string_set.txt"
    string_set = read_file(file_name)
    top_k = 3

    while True:
        search_word = input("Enter a word to search for (or type 'quit' to exit): ")

        if search_word.lower() == "quit":
            break

        similar_strings = perform_search(search_word, string_set, top_k)

        print(f"Top {top_k} similar strings to '{search_word}':")
        for string, score in similar_strings:
            print(f"{string}: {score}")

if __name__ == "_main_":
    main()