def main():
    path_to_book = "books/frankenstein.txt"
    with open(path_to_book) as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        print(f"The book contains {word_count} words")
        character_count = get_character_count(file_contents)
        print(f"The book contains {character_count}")

def get_word_count(file_contents):
    return len(file_contents.split())

def get_character_count(file_contents):
    counts = {}
    for character in file_contents.lower():
        if character not in counts:
            counts[character] = 0

        counts[character] += 1

    return counts

if __name__ == "__main__":
    main()
