import os
import pathlib


def create_directories():
     dir = os.path.dirname(os.path.abspath(__file__))
     for i in range(1, 10):
        directory_name = f"dir_{i}"
        pathlib.Path(f'{dir}/{directory_name}').mkdir(parents=True, exist_ok=True)
     for i in range(1, 10):
        if pathlib.Path(f'{dir}/{directory_name}').exists(): 
            print (f'dir_{i} created')
        else:
            print (f'dir_{i} deleted')

def remove_directories():
    dir = os.path.dirname(os.path.abspath(__file__))
    for i in range(1, 10):
        directory_name = f"dir_{i}"
        pathlib.Path(f'{dir}/{directory_name}').rmdir()
    for i in range(1, 10):
        if pathlib.Path(f'{dir}/{directory_name}').exists(): 
            print (f'dir_{i} created')
        else:
            print (f'dir_{i} deleted')


create_directories()
remove_directories()


