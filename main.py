import sys
from stats import (
    get_book_text,
    get_word_count,
    get_characters,
    create_list,
    sort_on,
)

def print_report(book_path, word_num, list_of_dicts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")
    for item in list_of_dicts:
        ch = item["char"]
        num = item["num"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {num}")
    print("============= END ===============")


def main():
    #Guard
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        contents = get_book_text(book_path)
        word_num = get_word_count(contents)
        character_count = get_characters(contents)
        list_of_dicts = create_list(character_count)
        list_of_dicts.sort(reverse=True, key=sort_on)
        print_report(book_path, word_num, list_of_dicts)
        
main()