def main():
    path_to_book = "books/frankenstein.txt"
    file_contents = read_file(path_to_book)

    word_count = get_word_count(file_contents)

    character_counts = get_character_counts(file_contents)
    character_frequencies = to_list_of_dicts(character_counts)
    character_frequencies.sort(reverse=True, key=sort_on)

    print_report(path_to_book, word_count, character_frequencies)


def print_report(path_to_book, word_count, character_frequencies):
    print(f"Reporting on {path_to_book}")
    print(f"The file contains {word_count} words.")
    print()
    for freq in character_frequencies:
        character = freq["char"]
        count = freq["count"]
        print(f"The '{character}' character is found {count} times")


def read_file(file_path):
    with open(file_path) as f:
        return f.read()


def get_word_count(file_contents):
    return len(file_contents.split())


def get_character_counts(file_contents):
    counts = {}
    for character in file_contents.lower():
        if character not in counts:
            counts[character] = 0

        counts[character] += 1

    return counts


def to_list_of_dicts(dict):
    result = []
    for key in dict:
        if key.isalpha():
            result.append({"char": key, "count": dict[key]})
    return result


def sort_on(dict):
    return dict["count"]


if __name__ == "__main__":
    main()
