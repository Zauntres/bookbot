def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    print(text)
    print (count_words(text), "words found in the dokument")

def read_book(path):
    with open(path) as f:
       return f.read()
    
def count_words(text):
    words = text.split()
#    word_count = 0
#   for word in words:
#        word_count += 1
#    return word_count
    return len(words)

main()