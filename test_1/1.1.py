while True:
    num = input("Введите число:")
    if num.isdigit():
        print(int(num) + 2)
        break
    else:
        print("не является числом")


#num = input("Введите число: ")
#i = 2
#if num.isdigit():
#    print(int(num)+i)
#else:
#    print("не является числом")
#оставил оба варианта, с циклом и без