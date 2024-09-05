def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    print(text)

def read_book(path):
    with open(path) as f:
       return f.read()

main()