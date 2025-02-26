# 1
from operator import truediv
from os import times

def ex1(x):
    longest = ""
    while x > 0:
        num = input("Please Enter a String: ")
        if len(num) > len(longest):
            longest = num
        x -= 1
    return longest


# print (ex1(3))

# 2
def ex2(x, s):
    length = len(s)
    return s[0: x] + s[length - x: length]


# print (ex2(2, "abcdefg"))

# 3
def ex3(s):
    i = 0
    l = len(s)
    while i < l:
        j = i + 1
        while j < l:
            if s[i] == s[j]:
                return False
            j += 1
        i += 1
    return True


# print(ex3("abc"))

# 4
def ex4(x, s):
    new = ""
    i = 0
    l = len(s)
    while i < l:
        slices = s[i: i + x]
        if i // x % 2 != 0:
            slices = slices[::-1]
        new += slices

        i += x
    return new


# print(ex4(2, "abcdefgh"))