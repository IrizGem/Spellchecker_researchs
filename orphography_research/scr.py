import codecs
import os
import pandas as pd

path_to_dicts = os.path.join(os.path.normpath(os.environ['PATH'].split(':')[0] + os.sep + os.pardir),
                            'data', 'dicts')
filename = path_to_dicts + 'freq_dict/freqrnc2011.csv'
df_3 = pd.read_csv(filename, sep='\t')
# print(df_3)
dict_words = {}

for i in range(df_3.shape[0]):
    if df_3['Lemma'][i].count('-') > 0 or df_3['Lemma'][i].count(' ') > 0:
        continue
    if df_3['Lemma'][i] in dict_words.keys():
        dict_words[df_3['Lemma'][i]] += df_3['Doc'][i]
        continue
    dict_words[df_3['Lemma'][i]] = df_3['Doc'][i]

# print(dict_words)
with open(path_to_dicts + 'plain_dict.txt', 'w') as file:
    for key in dict_words.keys():
        file.write(key + ' ' + str(dict_words[key]) + '\n')


# df_1 = pd.read_csv(path_to_dicts + 'russian_names.csv', sep=';')
# df_2 = pd.read_csv(path_to_dicts + 'russian_surnames.csv', sep=';')
#
# words_name = df_1['Name'].tolist()
# words_surname = df_2['Surname'].tolist()
# counts_name = df_1['PeoplesCount'].tolist()
# counts_surname = df_2['PeoplesCount'].tolist()
#
# with codecs.open(path_to_dicts + 'russian_all_dict.csv', 'w', 'utf-8') as file:
#     for i in range(len(words_name) + len(words_surname)):
#         if i < len(words_name):
#             if words_name[i].count(' ') > 0 or words_name[i].count('-') > 0:
#                 continue
#             line = words_name[i] + ' ' + str(counts_name[i]) + '\n'
#             file.write(line)
#         else:
#             ind = i - len(words_name)
#             print(ind)
#             if words_surname[ind].count(' ') > 0 or  words_surname[ind].count('-') > 0:
#                 continue
#             line = words_surname[ind] + ' ' + str(counts_surname[ind]) + '\n'
#             file.write(line)
