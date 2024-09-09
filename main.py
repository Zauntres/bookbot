def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    print(text)
    print (count_words(text), "words found in the dokument")
    print(letter_count(text))

def read_book(path):
    with open(path) as f:
       return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    #words = text.split()
    characters = {}
    for word in text:
        lower_string = word.lower()
        if lower_string in characters:
            characters[lower_string]+= 1
        else:
            characters[lower_string] = 1
    return characters



main()