# task 1
print("-----------------------------\nTASK_1")
a: list = [2, 3, 5, 0]
print("init list:", a)
a.remove(max(a))
print("second highest:", max(a))

# task 2
print("-----------------------------\nTASK_2")
a: list = [2, 3, 3, 3, 5, 5, 2, 2, 2, 2, 2, 0]
print("init list:", a)

tmp_num = a[0]
max_count = 1
tmp_count = 1
for item in range(1, len(a)):
    if a[item] == tmp_num:
        tmp_count += 1
        if tmp_count > max_count:
            max_count = tmp_count
    else:
        tmp_count = 1

    tmp_num = a[item]

print("max_count:", max_count)

# task 3
print("-----------------------------\nTASK_3")
a: list = [2, 3, 0, 3, 0, 3, 5, 5, 2, 2, 2, 2, 2, 0]
print("init list:", a)

for item in a:
    if item == 0:
        a.remove(item)
        a.append(0)
print("new a:", a)

# task 4
print("-----------------------------\nTASK_4")
a: list = [2, 3, 0, 3, 0, 11, 3, 5, 5, 2, 2, 2, 2, 2, 0]
print("init list:", a)


def make_dict(lst: list) -> dict:
    tmp_dict: dict = {lst[0]: 0}

    for item in lst:
        if item in tmp_dict:
            # print(tmp_dict[item])
            tmp_dict[item] = -1
        else:
            tmp_dict[item] = 1

    print("tmp_counter", tmp_dict)
    return tmp_dict


tmp = make_dict(a)
print(list(tmp.keys())[list(tmp.values()).index(1)])

# task 5
print("-----------------------------\nTASK_5")
a: list = [2, 1, 1]
print("init list:", a)

if a[0] == a[1] == a[2]:
    print(3)
elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    print(2)
else:
    print(0)

