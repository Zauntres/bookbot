def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
#    print(text)
    print (count_words(text), "words found in the dokument")
    print(letter_count(text))

def read_book(path):
    with open(path) as f:
       return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    words = text.split()
    for word in words:
        lower_string = word.lower()
        count = 0
        alphabet = {""}
        print(lower_string)
        for letter in lower_string:
                count += 1
                alphabet.add(letter)
        print(count)
        print(alphabet)

"""
charakter = {
    "a" = 3;
    "b" = 0,
    "c" = 0,
    ...
}
print(charakter[a]) --> 3
"""


main()