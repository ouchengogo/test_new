from bs4 import BeautifulSoup
import os
import requests
import re

#获取图片链接
r1 = requests.get("http://699pic.com/nature.html")
soup = BeautifulSoup(r1.content, "html.parser")
#根据class属性获取图片链接，注class_写
tag_image = soup.find_all(class_="lazy")
i = tag_image[0]
r2 = requests.get(i["data-original"])
print(r2.content)
