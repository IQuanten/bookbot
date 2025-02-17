def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars_dict = get_char_num_dict(text)
    print_book_report(book_path, num_words, num_chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_num_dict(text):
    charCount = {}
    text = text.lower()
    for char in text:
        if char not in charCount:
            charCount[char] = 1
        else:
            charCount[char] += 1
    return charCount

def print_book_report(book_path, num_words, num_chars_dict):
    print(book_path)
    print(f"{num_words} words found in the document")
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    for letter in alphabet:
        print(f"The '{letter}' character was found {num_chars_dict[letter]} times")

main()
