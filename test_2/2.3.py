my_list_1 = [2, 2, 5, 12, 8, 2, 12]
s = list()
for e in my_list_1:
    if my_list_1.count(e)==1:
        s.append(e)
print(s)

# Задача:
# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
