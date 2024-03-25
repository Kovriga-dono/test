my_list_1 = [2, 2, 5, 12, 8, 2, 12]
s = list()
for e in my_list_1:
    if my_list_1.count(e)==1:
        s.append(e)
print(s)