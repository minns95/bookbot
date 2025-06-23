import sys 

if len(sys.argv) != 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)
book_path = sys.argv[1]

from stats import get_word_count
from stats import get_book_text
from stats import get_char_count
from stats import sort_descending

def main():
    
    book_stored =get_book_text(book_path)
    word_count =get_word_count(book_stored)
    char_count = get_char_count(book_stored)
    sorted_chars = sort_descending(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for items in sorted_chars:
     print(f"{items['char']}: {items['num']}")
    print("============= END ===============")

main()
