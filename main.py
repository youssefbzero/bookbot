import sys

from stats import get_num_words ,get_count_char,get
def get_book_text(path):
    o = 'oh'
    with open(path) as f :
        o = f.read() 
    return o

def main(path):
    get(get_book_text(path))
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])

# Prints ['main.py', 'books/frankenstein.txt']
