def main():
    file_path = '/home/entropy/workspace/github.com/venkat-p29/bookbot/books/frankenstein.txt'
    text = file_contents(file_path)
    word_count = number_of_words(text)
    char_report = count_characters(text)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    print(char_report)
    print("--- End report ---")


def count_characters(text):
    my_text = text.lower()
    list_of_char = list(set(my_text))
    char_count = {}
    for char in list_of_char:
        char_count[char] = 0
    for char in my_text:
        if char in list_of_char:
            char_count[char] += 1
    
    char_report = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in char_count:
        if char in alphabet:
            char_report += f"The '{char}' was found {char_count[char]} times\n"
    return char_report
    

def file_contents(file_path):
    with open(file_path) as f:
        return f.read()


def number_of_words(text):
    words = text.split()
    return len(words)


main()