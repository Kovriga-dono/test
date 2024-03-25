name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Ваш вес: '))
if 50 < weight < 120:
        print('хорошее состояние')
else:
    if age < 40:
        print('следует заняться собой')
    else:
       print('следует обратиться к врачу!')