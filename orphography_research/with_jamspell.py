import os
import jamspell

path = ''  # set path_to_dicts if it's nessesary
g_corrector = jamspell.TSpellCorrector()
g_corrector.LoadLangModel(os.path.join(path, 'ru_small.bin'))


def clear_text(text):
    return g_corrector.FixFragment(text)


def clear_text_and_print(text):
    corrected = g_corrector.FixFragment(text)
    print(corrected)
    return corrected


if __name__ == '__main__':
    clear_text_and_print('абраззивный')
