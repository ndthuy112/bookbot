def main():
    file_path = "books/frankenstein.txt"
    #print(get_text(file_path))
    #print(count_words(file_path))
    #print(count_letters(file_path))
    create_report(file_path)


def get_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(file_path):
    file_contents = get_text(file_path)
    words = file_contents.split()
    return len(words)


def count_letters(file_path):
    file_contents = get_text(file_path).lower()
    letter_counts = {}
    for letter in file_contents:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


def create_report(file_path):
    word_count = count_words(file_path)
    letter_counts = count_letters(file_path)
    sorted_letters = (sorted(letter_counts, key = lambda x:letter_counts[x], reverse = True))

    print(f"This text file has {word_count} words")
    for letter in sorted_letters:
        if letter.isalpha():
            print(f"Letter {letter} appeared {letter_counts[letter]} times")

    
main()