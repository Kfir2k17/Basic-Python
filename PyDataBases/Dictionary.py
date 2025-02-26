# 1
def ex1(x):
    dic = {}
    i = 0
    while i < x:
        key = input(f"Enter Key {i + 1}: ")
        value = input(f"Enter Value {i + 1}: ")
        dic[key] = value
        i += 1

    return dic


# print(ex1(3))

# 2
def ex2(ls, x):
    dic = {}
    i = 0
    l = len(ls)
    while i < l:
        dic[ls[i]] = tuple(ls[i + 1: i + x])
        i += x

    return dic


# print(ex2([10, 30, 50, 20, 70, 90, 85, 60, 65, 15, 33, 47], 3))

# 3
def ex3(d):
    l = 0
    for key in d:
        l1 = len(d[key])
        if not l == 0:
            if not l == l1:
                return False
        l = l1
    return True


# print(ex3({10 : [30, 50, 23], 20 : [70, 80 ,90], 85 : [60, 65, 47] }))

# 4
def ex4(d1, d2):
    count = 0
    for entry1 in d1.items():
        for entry2 in d2.items():
            if entry1 == entry2:
                count += 1
    return count


# print(ex4({1: 2, 3: 4, 5: 7}, {1: 2, 3: 4, 4: 7}))

# 5
def ex5(x, y):
    for entry1 in x.items():
        k1 = entry1[0]
        v1 = entry1[1]

        if v1[0] == 1 and k1 in y:
            y.pop(k1)

        elif v1[0] == 2:
            b = v1[1]
            c = v1[2]

            for entry2 in y.items():
                k2 = entry2[0]
                if k2 == k1:
                    handler(entry2[1], b, c)

def handler(v2, b, c):
    i = 0
    l = len(v2)
    if b == 1:
        while i < l:
            v2[i] += c
            i += 1

    elif b == 2:
        while i < l:
            v2[i] -= c
            i += 1

    elif b == 3:
        while i < l:
            v2[i] *= c
            i += 1

    elif b == 4:
        while i < l:
            v2[i] //= c
            i += 1



X = {10: [1], 8: [2, 4, 3], 2: [0], 70: [2, 1, 9], 7: [1]}
Y = {2: [3, 20], 7: [65, 24, 30], 8: [9, 3, 6]}  # {2: [3, 20], 8: [3, 1, 2]}

ex5(X, Y)
print(Y)
