import random
import os
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
        if len(word) <= 4:
            return word
        return word[:min(ind, len(word) - 1)] + word[ind + 1:]


def poor_file_reader(filename, has_count_col=True, has_header=False, sep=' ', edge=20000):
    df_data = pd.DataFrame()
    if not os.path.isfile(filename):
        print('Wrong path')
        return df_data
    if os.path.splitext(filename)[1] == '.csv':
        if has_count_col and not has_header:
            df_data = pd.read_csv(filename, sep=sep, header=None)
            df_data.columns = ['word', 'count']
            df_data = pd.DataFrame(df_data.loc[df_data['count'] >= edge])
        elif has_count_col and has_header:
            df_data = pd.read_csv(filename, sep=sep)
            df_data = pd.DataFrame(df_data.loc[df_data['count'] >= edge])
        elif not has_count_col and not has_header:
            df_data = pd.read_csv(filename, sep=sep, header=None)
            df_data = df_data.iloc[0]
        elif not has_count_col and has_header:
            df_data = pd.read_csv(filename, sep=sep)
            key = 'word'
            if key not in df_data.columns:
                key = 'name'
            if key not in df_data.columns:
                key = 'text'
            if key not in df_data.columns:
                key = ''
            if key != '':
                df_data = df_data.loc[df_data[key]]
                df_data.columns = ['word']
            else:
                df_data = df_data.iloc[0]
                df_data.columns = ['word']
    else:
        print('Sorry, cannot read this file')
    return df_data


def generate_spoiled_data(df_data,
                          morph_list,
                          max_one_name=5,
                          num_substitution=1):
    if 'word' not in df_data.columns:
        print('No data frame')
        return None

    true_names = df_data['word'].tolist()
    true_names_labels = []

    num_sets = len(morph_list)
    all_spoiled_names = []
    for i in range(num_sets):
        all_spoiled_names.append([])
    for name in true_names:
        name = name.lower()
        num_for_name = random.randint(0, max(max_one_name, 0))
        for i in range(num_for_name):
            true_names_labels.append(name.capitalize())
            for k_set in morph_list:
                spoiled_name = name
                for j in range(max(num_substitution, 1)):
                    ind = random.randint(0, len(k_set)-1)
                    k = k_set[ind]
                    spoiled_name = commit_metamorph(spoiled_name, k)
                all_spoiled_names[morph_list.index(k_set)].append(spoiled_name.capitalize())

    df_test_data = pd.DataFrame({'word': true_names_labels})
    for i in range(num_sets):
        df_test_data[i+1] = all_spoiled_names[i]

    return df_test_data


if __name__ == '__main__':
    path = '/home/iris/Repos/venviroments/orphograpy_reasearch/data/dicts/russian_all_dict.csv'
    df = generate_spoiled_data(poor_file_reader(path), morph_list=[[0], [1], [2], [0, 1], [1, 2], [0, 2], [0, 1, 2]])
    print(df)
