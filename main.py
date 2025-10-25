from stats import word_count, get_book_text, character_count, character_count_sorted
import sys
def main():
    if sys.argv and len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book_path)
    print(f"Found {word_count(book_text)} total words")
    #print(character_count(book_text))

    for c in character_count_sorted(character_count(book_text)):
        if c["char"].isalpha():
            print(f"{c['char']}: {c['count']}")

main()
