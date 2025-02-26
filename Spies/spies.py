# בסד

"""spies exercise
Given logfiles, find the url pieces and downloads the images.

Here's what a url piece looks like:
10.254.254.28 - - [08/Aug/2016:00:13:48 -0700] "GET /cyberbit/a-baah.jpg. HTTP/1.0" 302 528 "-"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

import os
import re
import sys
import urllib
from tkinter import Image
from urllib import request
from PIL import Image

link = "https://ahohcs.files.wordpress.com/2018/10/"

def extract_urls(filename):
    ls = []
    log1 = open(filename, 'r')
    for line in log1:
        if "cyberbit" in line:
            words = line.split("/")
            url = link
            for word in words:
                if "pa-" in word:
                    ending = word[:len(word) - 5]
                    url += ending
                    break

                if "pp-" in word:
                    ending = word[:len(word) - 5]
                    url += ending
                    break

            if url not in ls:
                ls.append(url)
    if int(filename[-5]) == 2:
        ls.sort(key=lambda x: x[-8:])

    else:
        ls.sort()

    log1.close()
    return ls


def get_images(img_urls, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    os.chdir(dest_dir)

    i = 0
    l = len(img_urls)
    while i < l:
        filename = os.path.basename(img_urls[i])
        print(img_urls[i])
        request.urlretrieve(img_urls[i], filename)
        os.rename(os.path.basename(img_urls[i]), f"img{i}.jpg")
        i += 1

    os.chdir("..")

def create_photo(path, length):
    os.chdir(path)
    img = Image.open(f'img0.jpg')
    width, height = img.size
    pos = 0
    suspect_image = Image.new("RGB", ((width*length),height ))
    i = 0
    while i < length:
        img = Image.open(f'img{i}.jpg')
        suspect_image.paste(img, (pos, 0))
        pos += width
        i += 1
    suspect_image.show()
    suspect_image.save(f'suspect_image.jpg')
    os.chdir("..")

# get pics
urls1 = extract_urls("log_suspect1.log")
urls2 = extract_urls("log_suspect2.log")
get_images(urls1,"pics1") # לשמור את התמונות
get_images(urls2,"pics2") # לשמור את התמונות


create_photo("pics1", 20)
create_photo("pics2", 200)

# Web Solution
"""web = open("web.html", "w")
web.write("<html>\n<table id='table' cellspacing='0' cellpadding='0'>\n")
web.write("<tr>")
ind = 0
while ind < 20:
    web.write("<td>")
    web.write(f'<img src="pics1/img{ind}.jpg">')
    web.write("</td>\n")
    ind += 1

ind = 0
while ind < 200:
    web.write("<td>")
    web.write(f'<img src="pics2/img{ind}.jpg">')
    web.write("</td>\n")
    ind += 1

web.write("</tr>")

web.close()"""
