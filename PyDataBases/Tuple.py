# 1
def ex1(tp):
    l = len(tp)
    tp1 = (tp[0], tp[l // 2], tp[l - 1])
    if l % 2 == 0:
        tp1 = tp1 = (tp[0], (tp[l // 2] + tp[l // 2 - 1]) / 2, tp[l - 1])
    return tp1


# print(ex1((9, 7, 20, 5)))

# 2
def ex2(tp1, tp2):
    for item1 in tp1:
        found = False
        for item2 in tp2:
            if item1 == item2:
                found = True
        if not found:
            return False

    return True

# 3
def lastintp(tp):
    return tp[len(tp)-1]

def ex3(ls):
    ls.sort(key=lastintp)

"""
ls1 = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
ex3(ls)
print(ls)
"""

# 4
def ex4(ls):
    tp = tuple(x for x in ls)
    return tp