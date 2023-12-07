def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        text_lower = file_contents.lower()
        words = text_lower.split()
        num_words = get_num_words(file_contents)
        letter_count = get_letter_count()

def get_num_words(words):
# counts words
    word_count = 0
    for word in words:
        word_count += 1

def get_letter_count(words):
#count letters
    letter_count = {}
    for word in words:
        for letters in words:
            if letters in letter_count:
                letter_count[letters] += 1
            else:
                letter_count[letters] = 1

main()