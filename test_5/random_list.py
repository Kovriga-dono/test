import random

def get_random_elem():
    some_list = [1, 2]
    if len(some_list) != 0:
        print (random.choice(some_list))
    else:
        print('None')
get_random_elem()
