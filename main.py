from operator import attrgetter

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = get_num_words(words)
        letter_count = get_letter_count(words)
        sorted_list = get_sorted_list(letter_count)

        print("--- Book Report of Mary Shelly's Frankenstein ---")
        print(f"{num_words} words were found in the book")
        for item in sorted_list:
            if not item["char"].isalpha():
                continue
            print(f"The {item['char']} character was found {item['num']} times")
        print("--- End Report ---")

def get_num_words(words):
# counts words
    return len(words)

def get_letter_count(words):
#count letters
    letter_count = {}
    for word in words:
        lowered = word.lower()
        for w in lowered:
            if w.isalpha():
                if w in letter_count:
                    letter_count[w] += 1
                else:    
                    letter_count[w] = 1             
    return letter_count

def get_sorted_list(letter_count):
# turn dictionary to list then sorts
    sorted_list = []
    for letter in letter_count:
        sorted_list.append({"char": letter, "num": letter_count[letter]})  
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list  

def sort_on(d):
    return d["num"] 
#was in the provided solution and holds the sort function on shoulders, not 100% on how

main()