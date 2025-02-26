import os
import shutil
from bs4 import BeautifulSoup

# 1

def ex1():
    path = input("Please enter the path to the file: ")
    fl = open(path, "r")
    i = 0
    for line in fl:
        if i % 2 != 0:
            print(line.strip())
        i += 1
    fl.close()


# ex1()

# 2
def ex2():
    path = input("Please enter the path to the file: ")
    fl = open(path, "w")
    st = input("Please enter a string to the file: ")
    while not st == "":
        fl.write(st)
        st = input("Please enter a string to the file: ")
    fl.close()


# ex2()

# 3
def ex3(origin, target, x):
    org = open(origin, "r")
    tar = open(target, "w")
    lines = org.readlines()
    i = 0

    while i < x:
        for line in lines:
            if i >= x:
                break
            tar.write(line)
            i += 1

    tar.close()
    org.close()


ex3("text.txt", "jeez.txt", 6)


# 4
def ex4(ls):
    os.mkdir("A")
    os.mkdir("B")

    for item in ls:
        os.chdir(item[0])
        file = open(item[1], "w")
        i = 2
        l = len(item)
        while i < l:
            file.write(item[i] + "\n")
            i += 1
        os.chdir("..")
        file.close()


# ex4([["A", "test1.txt", "first line 1", "second line 1"], ["B", "test2.txt", "first line 2", "second line 2", "third line 2"]])

# 5
def ex5(origin, x):
    d = {}
    fl = open(origin, "r")
    for line in fl:
        d[line[0]] = line[4:x + 4]
    fl.close()
    return d


# print(ex5("dic.txt", 20))

# 6
def ex6(origin):
    handle = open(origin, "r")
    lines = handle.readlines()
    html = "".join(lines)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(["link", "script", "img"])
    list = []
    for tag in tags:
        if tag.has_attr('href'):
            list.append(tag['href'])
        if tag.has_attr('src'):
            list.append(tag['src'])


# 7
def ex7(origin, n):
    fl = open(origin, 'r')

    l = len(origin)
    t = origin[l - 4:]
    new = open(origin[:l - 4] + "_copy" + t, 'w')

    if t != ".txt":
        fl.close()
        fl = open(origin, 'rb')
        new.close()
        new = open(origin[:l - 4] + "_copy" + t, 'wb')

    new.write(fl.read(n))

    fl.close()
