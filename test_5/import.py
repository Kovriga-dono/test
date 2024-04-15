from main import create_directories 
from main import remove_directories
from random_list import get_random_elem

def call():
    get_random_elem()
    create_directories()
    remove_directories()

    call()


