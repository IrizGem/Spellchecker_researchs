import os
from textblob.en import Spelling
from rapidfuzz import fuzz

path_to_dict = os.path.join(os.path.normpath(os.environ['PATH'].split(':')[0] + os.sep + os.pardir),  'data', 'dicts', 'freq_dict', 'plain_dict.txt')
# print(path_to_dict)

spelling = Spelling(path_to_dict)


def __solver(word, suggestions):
    qualities = [fuzz.ratio(word, s) for s in suggestions]
    if len(qualities) > 0:
        return suggestions[qualities.index(max(qualities))][0]
    return word


def clear_word(word, use_solver=True):
    suggestions = spelling.suggest(word)
    if suggestions.count(word) > 0:
        return word
    if use_solver:
        return __solver(word, suggestions)
    else:
        return suggestions[0][0]


def clear_text(text):
    words = tokenizer(text)
    correct_words = []
    for word in words:
        correct_words.append(clear_word(word))
    corrected = ' '.join(correct_words)
    return corrected


def tokenizer(text):
    text.replace('.', ' ').replace(',', ' ')
    return text.split(' ')


if __name__ == '__main__':
    print(clear_text('абраззивный'))


