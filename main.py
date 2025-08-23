import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = get_num_words(text)
    char_count = get_char_count(text)
    print(f"Found {count} total words" )
    sorted = sort_count(char_count)
    for dict in sorted:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
main()