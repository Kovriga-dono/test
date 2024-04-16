import json
import pickle

my_favourite_group = {'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
{'name': 'Шапито', 'year': 2014}]}

json_data = json.dumps(my_favourite_group, ensure_ascii=False)
print(json_data)

with open('group.json', 'w', encoding='utf-8') as json_file:
    json.dump(my_favourite_group, json_file, ensure_ascii=False)


pickle_data = pickle.dumps(my_favourite_group)
print(pickle_data)

with open('group.pickle', 'wb') as pickle_file:
    pickle.dump(my_favourite_group, pickle_file)

# Задача:
# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал. 
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
