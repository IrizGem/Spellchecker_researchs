import random
import pandas as pd
letters = 'ёйцукенгшщзхъфывапролджэячсмитьбю'


def commit_metamorph(word, k):  # функция для искажения буквы в слове
    ind = random.randint(0, len(word))  # индекс искажаемой буквы
    letter = letters[min(random.randint(0, len(letters)), len(letters) - 1)]
    # k - тип искажения
    # 0 -> изменение буквы, 1 -> вставка буквы, 2 -> удаление буквы
    if k == 0:
        return word[:min(ind, len(word) - 1)] + letter + word[ind + 1:]
    if k == 1:
        return word[:ind] + letter + word[ind:]
    if k == 2:
        return word[:min(ind, len(word) - 1)] + word[ind + 1:]


def generate_spoiled_data(filename,  max_one_name=5, num_substitution=1, edge=20000):
    df_data = pd.read_csv(filename, sep=' ', header=None)
    df_data.columns = ['word', 'count']
    df_data = pd.DataFrame(df_data.loc[df_data['count'] >= edge])

    true_names = df_data['word'].tolist()
    true_names_labels = []
    all_spoiled_names = [[], [], []]
    for name in true_names:
        name = name.lower()
        num_for_name = random.randint(0, max(max_one_name, 0))
        for i in range(num_for_name):
            true_names_labels.append(name.capitalize())
            for k in range(0, 3):
                spoiled_name = name
                for j in range(max(num_substitution, 1)):
                    spoiled_name = commit_metamorph(spoiled_name, k)
                all_spoiled_names[k].append(spoiled_name.capitalize())

    df_test_data = pd.DataFrame({'word': true_names_labels,
                                 'changed': all_spoiled_names[0],
                                 'added': all_spoiled_names[1],
                                 'deleted': all_spoiled_names[2]})
    return df_test_data


if __name__ == '__main__':
    df = generate_spoiled_data('/home/iris/Repos/venviroments/orphograpy_reasearch/data/dicts/russian_all_dict.csv')
    print(df)
