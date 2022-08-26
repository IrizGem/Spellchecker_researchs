from textblob.en import Spelling
from rapidfuzz import fuzz
spelling = Spelling('/home/iris/Repos/venviroments/orphograpy_reasearch/data/dicts/freq_dict/plain_dict.txt')


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


