import random

def get_random_elem():
    some_list = [1, 2]
    if len(some_list) != 0:
        print (random.choice(some_list))
    else:
        print('None')
get_random_elem()


# Задача:
# Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
