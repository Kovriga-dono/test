from main import create_directories 
from main import remove_directories
from random_list import get_random_elem

def call():
    get_random_elem()
    create_directories()
    remove_directories()

#я вообще не уверен, что решение корректное, но, в таком виде все три функции вызываются в одном экземпляре

# Задача:
# Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. 
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.

