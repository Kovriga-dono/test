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