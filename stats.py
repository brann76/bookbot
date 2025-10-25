def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for char in text:
        char = char.lower()
        characters[char] = characters.get(char, 0) + 1
    return characters

def sort_on(items):
    return items["count"]

def character_count_sorted(dict_char_counts):
    char_count_list = [] #[{"char": char, "count": count} for char, count in dict_char_counts.items()]
    for char in dict_char_counts:
        char_count_list.append({"char": char, "count": dict_char_counts[char]})
    char_count_list.sort(key=sort_on, reverse=True)
    return char_count_list
