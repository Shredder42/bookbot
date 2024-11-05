def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_chars(text)
    create_report(book_path, word_count, character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_chars(text):
    count_dict = {}
    for char in text.lower():
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1
    return count_dict

def create_report(path, word_count, character_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for char in character_count:
        if char in ('abcdefghijklmnopqrstuvwxyz'):
            print(f"The '{char}' character was found {character_count[char]} times")
    print("--- End report ---")



main()




