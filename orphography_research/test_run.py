from tqdm import tqdm
from tqdm import trange
import my_metamorphs
import with_enchant
import with_jamspell
import with_textblob

path = '/home/iris/Repos/venviroments/orphograpy_reasearch/data/dicts/russian_all_dict.csv'
df_test = my_metamorphs.generate_spoiled_data(my_metamorphs.poor_file_reader(path, edge=50000),
                                              num_substitution=1,
                                              morph_list=[[0], [1], [2], [0, 1, 2]])
print(df_test)

print('\n###JAMSPELL###')
vec_cha_jamspell = []
vec_add_jamspell = []
vec_del_jamspell = []
vec_all_jamspell = []
vec_off_jamspell = []

run_j = trange(df_test.shape[0])
for i in run_j:
    vec_cha_jamspell.append(with_jamspell.clear_text(df_test[1][i]) == df_test['word'][i])
    vec_add_jamspell.append(with_jamspell.clear_text(df_test[2][i]) == df_test['word'][i])
    vec_del_jamspell.append(with_jamspell.clear_text(df_test[3][i]) == df_test['word'][i])
    vec_all_jamspell.append(with_jamspell.clear_text(df_test[4][i]) == df_test['word'][i])
    vec_off_jamspell.append(with_jamspell.clear_text(df_test['word'][i]) == df_test['word'][i])

    acc1 = round(sum(vec_cha_jamspell) / len(vec_cha_jamspell), 3)
    acc2 = round(sum(vec_add_jamspell) / len(vec_add_jamspell), 3)
    acc3 = round(sum(vec_del_jamspell) / len(vec_del_jamspell), 3)
    acc4 = round(sum(vec_all_jamspell) / len(vec_all_jamspell), 3)
    acc5 = round(sum(vec_off_jamspell) / len(vec_off_jamspell), 3)
    # run_j.set_description(f'(cha={acc1}, add={acc2}, del={acc3}, all={acc4}, without={acc5})')
    run_j.set_description(f'(all={acc4}, without={acc5})')

print()
print('Изменённые буквы', sum(vec_cha_jamspell)/len(vec_cha_jamspell))
print('Добавленные буквы', sum(vec_add_jamspell)/len(vec_add_jamspell))
print('Удалённые буквы', sum(vec_del_jamspell)/len(vec_del_jamspell))
print('Все изменения', sum(vec_all_jamspell)/len(vec_all_jamspell))
print('Изменения отсутствуют', sum(vec_off_jamspell)/len(vec_off_jamspell))

print('\n###ENCHANT###')
vec_cha_enchant = []
vec_add_enchant = []
vec_del_enchant = []
vec_all_enchant = []
vec_off_enchant = []

run_e = trange(df_test.shape[0])
for i in run_e:
    vec_cha_enchant.append(with_enchant.clear_word(df_test[1][i], False) == df_test['word'][i])
    vec_add_enchant.append(with_enchant.clear_word(df_test[2][i], False) == df_test['word'][i])
    vec_del_enchant.append(with_enchant.clear_word(df_test[3][i], False) == df_test['word'][i])
    vec_all_enchant.append(with_enchant.clear_word(df_test[4][i], False) == df_test['word'][i])
    vec_off_enchant.append(with_enchant.clear_word(df_test['word'][i], False) == df_test['word'][i])

    acc1 = round(sum(vec_cha_enchant) / len(vec_cha_enchant), 3)
    acc2 = round(sum(vec_add_enchant) / len(vec_add_enchant), 3)
    acc3 = round(sum(vec_del_enchant) / len(vec_del_enchant), 3)
    acc4 = round(sum(vec_all_enchant) / len(vec_all_enchant), 3)
    acc5 = round(sum(vec_off_enchant) / len(vec_off_enchant), 3)
    # run_e.set_description(f'(cha={acc1}, add={acc2}, del={acc3}, all={acc4}, without={acc5})')
    run_e.set_description(f'(all={acc4}, without={acc5})')

print()
print('Изменённые буквы', sum(vec_cha_enchant)/len(vec_cha_enchant))
print('Добавленные буквы', sum(vec_add_enchant)/len(vec_add_enchant))
print('Удалённые буквы', sum(vec_del_enchant)/len(vec_del_enchant))
print('Все изменения', sum(vec_all_enchant)/len(vec_all_enchant))
print('Изменения отсутствуют', sum(vec_off_enchant)/len(vec_off_enchant))

print('\n###TEXTBLOB###')
vec_cha_textblob = []
vec_add_textblob = []
vec_del_textblob = []
vec_all_textblob = []
vec_off_textblob = []

run_t = trange(df_test.shape[0])
for i in run_t:
    vec_cha_textblob.append(with_textblob.clear_word(df_test[1][i], False) == df_test['word'][i])
    vec_add_textblob.append(with_textblob.clear_word(df_test[2][i], False) == df_test['word'][i])
    vec_del_textblob.append(with_textblob.clear_word(df_test[3][i], False) == df_test['word'][i])
    vec_all_textblob.append(with_textblob.clear_word(df_test[4][i], False) == df_test['word'][i])
    vec_off_textblob.append(with_textblob.clear_word(df_test['word'][i], False) == df_test['word'][i])

    acc1 = round(sum(vec_cha_textblob) / len(vec_cha_textblob), 3)
    acc2 = round(sum(vec_add_textblob) / len(vec_add_textblob), 3)
    acc3 = round(sum(vec_del_textblob) / len(vec_del_textblob), 3)
    acc4 = round(sum(vec_all_textblob) / len(vec_all_textblob), 3)
    acc5 = round(sum(vec_off_textblob) / len(vec_off_textblob), 3)
    # run_t.set_description(f'(cha={acc1}, add={acc2}, del={acc3}, all={acc4}, without={acc5})')
    run_t.set_description(f'(all={acc4}, without={acc5})')

print()
print('Изменённые буквы', sum(vec_cha_textblob)/len(vec_cha_textblob))
print('Добавленные буквы', sum(vec_add_textblob)/len(vec_add_textblob))
print('Удалённые буквы', sum(vec_del_textblob)/len(vec_del_textblob))
print('Все изменения', sum(vec_all_textblob)/len(vec_all_textblob))
print('Изменения отсутствуют', sum(vec_off_textblob)/len(vec_off_textblob))
