import json
import pickle
import os

path = 'group.json'
if os.path.exists(path):
    with open('group.json', encoding='utf-8') as f:
        data = json.load(f)
        print(data)
else:
  print("JSON doesn't exist!")



path = 'group.pickle'
if os.path.exists(path):
    with open('group.pickle', 'rb') as fh:
        datap = pickle.load(fh)
        print (datap)
else:
    print("pickle doesn't exist!")

# Задача:
# Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию. 
# И получить объект: словарь из предыдущего задания.
