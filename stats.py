def get_word_count(book_text):
    split_words = book_text.split()
    num_words = len(split_words)
    return num_words

def get_book_text(file_path):
    with open(file_path) as f:
        contents_string = f.read()
    return contents_string

def get_char_count(book_text):
    char_dict = {}
    lower_text =book_text.lower()

    for chars in lower_text:
        if chars in char_dict:
            char_dict[chars] += 1
        else:
            char_dict[chars] = 1

    return char_dict

#char_count = get_char_count()

def get_value(items):
    return items["num"]

def sort_descending(char_count):
    sorted_list = []
    for char, count in char_count.items():
        if char.isalpha():
            count_num_dict = {"char": char, "num": count}
            sorted_list.append(count_num_dict)

    sorted_list.sort(reverse = True, key= get_value)

    return sorted_list