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
    words = text.split()
    alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"} 
    characters = {}
    for word in words:
        lower_string = word.lower()
        count = 0
        #print(lower_string)
        for letter in lower_string:
            print(letter)
            if letter in alphabet:
                count += 1
            #alphabet.add(letter)
            characters[letter[0]] = count
       # print(count)
   # print(alphabet)
    print(characters)

"""
character = {
    "a" = 3;
    "b" = 0,
    "c" = 0,
    ...
}
print(character[a]) --> 3
"""


main()