import re


def get_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().split(' ')


def get_words_from_text(text):
    return re.findall(r'[A-Za-z0-9]+', text.lower())


def count_words(words_to_search, words, words_counts):
    for word in words_to_search:
        words_counts[word] += words.count(word)


def get_words_counts(file_path, words):
    words_counts = {word: 0 for word in words}

    with open(file_path, 'r') as file:
        for line in file:
            words_in_line = get_words_from_text(line)
            count_words(words, words_in_line, words_counts)
    return words_counts


def print_words_counts(words_counts):
    def order_by_value(pair):
        (key, value) = pair
        return (value, key)

    sorted_words_counts = sorted(
        words_counts.items(),
        key=order_by_value,
        reverse=True)
    [print(f'{word} - {count}') for (word, count) in sorted_words_counts]


words_file_path = './files/Words Count/words.txt'
text_file_path = './files/Words Count/text.txt'

words_counts = get_words_counts(text_file_path, get_words_from_file(words_file_path))
print_words_counts(words_counts)
print(words_counts)
