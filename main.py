
def read_book():
    book = "/home/zauntres/bookbot/github.com/zauntres/bookbot/books/frankenstein.txt"
    with open(book) as f:

        file_contents = f.read()

        print(file_contents)

def main():

    read_book()

main()