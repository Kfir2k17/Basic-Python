from math import sin, cos, tan, pi
import os
from urllib import request
from PIL import Image

# 1
def ex1(start, end, x):
    if x == 1:
        while start <= end:
            print(sin(start))
            start += 1

    elif x == 2:
        while start <= end:
            print(cos(start))
            start += 1

    elif x == 3:
        while start <= end:
            print(tan(start))
            start += 1

# 2
def ex2(d, t):
    name_ls = os.listdir(d)
    l = len(name_ls)
    i = 1
    os.chdir(d)
    while i <= l:
        if name_ls[i-1][len(name_ls[i-1])-3:] == t:
            os.rename(name_ls[i-1], f"{i}.{t}")
        i+= 1

    os.chdir("..")

# 3
def ex3(ls):
    for item in ls:
        ending = os.path.splitext(item)[1][1:]

        if not os.path.exists(ending):
            os.makedirs(ending)
        filename = os.path.basename(item)
        filepath = os.path.join(ending, filename)

        request.urlretrieve(item, filepath)

# lst = ["https://media.reshet.tv/image/upload/t_grid-item-large/v1656511046/uploads/2022/903140184.webp",
#      "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Vervet_monkey_Krugersdorp_game_reserve_%285657678441%29.jpg/345px-Vervet_monkey_Krugersdorp_game_reserve_%285657678441%29.jpg"]
# ex3(lst)

# 4
def ex4(fn):
    img = Image.open(fn)
    new = img.rotate(180)
    new.save("new.png")
    img.close()

# ex4("unnamed.png")

# 5
def ex5(fn1, fn2):
    with Image.open(fn1) as img1, Image.open(fn2) as img2:
        great_image = Image.new("RGB", (1000, 1000))
        w = img1.width
        h = img1.height
        great_image.paste(img2 , (0, 0))
        great_image.paste(img1, (w, 0))
        great_image.paste(img1, (0, h))
        great_image.paste(img2, (w, h))
        great_image.show()

ex5("unnamed.png", "new.png")
