def read_text_from_path(path: str) -> str:
    with open(path) as f:
        return f.read()


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_chars(text: str) -> dict[str, int]:
    letter_counts = {}
    for letter in text.lower():
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    sorted_letter_counts = dict(sorted(letter_counts.items()))
    return sorted_letter_counts


def main() -> None:
    book_path = "books/frankenstein.txt"
    text = read_text_from_path(book_path)
    num_words = count_words(text)
    num_chars = count_chars(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for letter, count in num_chars.items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
