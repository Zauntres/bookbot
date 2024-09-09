def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    #print(text)
    print(f"--- Begin report of {book_path} ---")
    print (count_words(text), "words found in the dokument")
#    print(letter_count(text))
    print(sorting_characters(letter_count(text)))

def read_book(path):
    with open(path) as f:
       return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    characters = {}
    for word in text:
        lower_string = word.lower()
        if lower_string in characters:
            characters[lower_string]+= 1
        else:
            characters[lower_string] = 1
    return characters

def sorting_characters(dict):
    sort_out = {}
    for chars in dict:
        char_list = chars.split()
        for letter in char_list:
            if letter.isalpha():
                sort_out[char_list[0]] = dict[chars] 
    rsort = sorted(sort_out, key=lambda sort_out: sort_out)
    return sort_out


main()