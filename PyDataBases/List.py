# 1
def ex1(x):
    ls = []
    i = 0
    while i < x:
        ls.append(int(input(f"Please enter number {i + 1} to the list: ")))
        i += 1
    return ls


# print(ex1(3))

# 2
def ex2(ls1, x):
    for item in ls1:
        if item % x != 0:
            ls1.remove(item)


# print(ex2([10, 6, 20, 9, 15], 3))

# 3
def ex3(ls):
    i = 1
    l = len(ls)
    while i < l:
        if ls[i] < ls[i - 1]:
            return False
        i += 1
    return True


# print(ex2([2, 3, 4]))

# 4
def ex4(ls):
    longest = 0
    place = 0
    i = 0

    length = 0
    current_place = 0
    accel = False

    l = len(ls)
    while i < l - 1:
        if accel:
            if ls[i] < ls[i + 1]:
                length += 1

            else:
                accel = False
                if length > longest:
                    longest = length
                    place = current_place

        if not accel:
            if ls[i] < ls[i + 1]:
                accel = True
                current_place = i
                length = 2
        i += 1

    return longest, place


# print (ex4([10, 20, 9, 15, 23, 25, 21, 37, 30, 3]))

# 5
def ex5(ls):
    ls2, pre = [ls[0]], ls[0]
    for item in ls:
        if item > pre:
            ls2.append(item)
            pre = item
    return ls2


# print(ex5([10, 20, 9, 15, 23, 21, 37, 30, 35]))

# 6
def ex6(ls1, ls2):
    ls3 = [ls1[0]]
    i = 1
    l1, l2 = len(ls1), len(ls2)
    l = l1 + l2
    i1 = 1
    i2 = 0

    while i < l:
        if i % 2 == 0 and i1 < l1 or i2 >= l2 and i1 < l1:
            ls3.append(ls1[i1])
            i1 += 1

        if not i % 2 == 0 and i2 < l2 or i1 >= l1 and i2 < l2:
            ls3.append(ls2[i2])
            i2 += 1

        i += 1

    return ls3


# print(ex6([1, 3, 5, 7, 9, 10, 11, 12], [2, 4, 6, 8]))

# 7
def ex7(ls):
    l = len(ls)
    ls1 = ls[l // 2:] + ls[:l // 2]
    return ls1


# print(ex7([10, 20, 50, 40]))

# 8
def ex8(x, ls):
    i = 0
    l = len(ls)
    ls1 = []
    while i * x < l:
        place = i * x
        ls1.append(ls[place: place + x])
        i += 1
    return ls1


# print(ex8(1, [10, 20, 30, 40, 50, 60, 70, 80, 90]))

# 9
def ex9(ls):
    l = len(ls)
    ls1, ls2 = ls[:l // 2], ls[l // 2:]
    ls1.sort()
    ls2.sort(reverse=True)
    return ls1 + ls2


# print(ex9([50, 63, 40, 77, 9, 20,15, 8]))

# 10
def sum_num(item):
    s = 0
    while item > 0:
        s += item % 10
        item //= 10
    return s


def ex10(ls):
    ls.sort(key=sum_num)


"""
ls1 = [93, 25, 14, 43, 800]
ex10(ls1)
print(ls1)
"""


# 11
def middle(item):
    l = len(str(item))
    i = 0
    while i < l // 2:
        item //= 10
        i += 1

    return item % 10



def ex11(ls):
    ls.sort(key=middle, reverse=True)

"""
ls2 = [973, 205, 4, 43623, 8, 777]
ex11(ls2)
print(ls2)
"""