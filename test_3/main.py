#Угадай число
n1, n2 = 1, 100
while True:
    x = (n1+n2)//2
    print('Твое число больше, меньше или равно', x,'?')
    n = (input('< - Больше, > - Меньше, = - Равно:  '))
    if n == '>':
        n2 = x
    elif n == '<':
        n1 = x
    elif n == '=':
        print('Я угадал')
        break
    else:
        print('Введен не верный символ')

# Задача:
# В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. Компьютер начинает его отгадывать предлагая игроку варианты чисел. 
# Если компьютер угадал число, игрок выбирает “победа”. Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”. 
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.
# Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры для общения с компьютером. Вы можете использовать этот способ или придумать свой.
