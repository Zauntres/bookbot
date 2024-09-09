
def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    #print(text)
    print(f"--- Begin report of {book_path} ---")
    print (count_words(text), "words found in the dokument")
#    print(letter_count(text))
    print(sorting_characters(letter_count(text)))
    for zeichen in sorting_characters(letter_count(text)):
        number = sorting_characters[zeichen]
        print(f"The {zeichen} character was found {number} times")

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
    sort_out_out = {}
# Create a new dictionary for alphabetic characters only
    for chars in dict:   
        if chars.isalpha():
            sort_out[chars] = dict[chars] 
# Sort the dictionary by frequency of occurrence (the values), in descending order
    rsort = sorted(sort_out.items(), reverse=True, key=lambda item: item[1])
    #print(rsort)

# Convert the sorted list of tuples back into a dictionary if needed   
    sort_out_out = {letter: count for letter, count in rsort}
   
    return sort_out_out

"""
    for letter in rsort:
        sort_out_out = sort_out[letter]
        print(sort_out_out, "for")
    print(sort_out)
""" 

main()
