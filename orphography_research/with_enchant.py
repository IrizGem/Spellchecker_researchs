from rapidfuzz import fuzz
import enchant
g_dictionary = enchant.Dict("ru_RU")


def __solver(word, suggestions):
    qualities = [fuzz.ratio(word, s) for s in suggestions]
    if len(qualities) > 0:
        return suggestions[qualities.index(max(qualities))]
    return word


def clear_word(word, use_solver=True):
    if not g_dictionary.check(word):
        suggestions = g_dictionary.suggest(word)
        if use_solver:
            return __solver(word, suggestions)
        elif len(suggestions) > 0:
            return suggestions[0]
    return word


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
