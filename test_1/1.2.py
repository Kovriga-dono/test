while True:
    rand = input("Введите число:")
    if rand.isdigit() and 0 < int(rand) <11:
        print(int(rand) ** 2)
        break
    elif rand.isdigit():
        print('число должно быть больше 0 и меньше 10')
    else:
        print("не является числом")


#Задача:
#Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
