from bs4 import BeautifulSoup
import os
import requests
import re

#获取图片链接
r1 = requests.get("http://699pic.com/nature.html")
soup = BeautifulSoup(r1.content, "html.parser")
#根据class属性获取图片链接，注class_写
tag_image = soup.find_all(class_="lazy")
#属性data-original存放图片路径，title为图片名称，通过这些关键字就能获取到对应图片

#确定存储图片的路径
chengxuwenjian_path = os.path.realpath(__file__)
dangqian_path = os.path.dirname(chengxuwenjian_path)  # jiekou_sample
# 使用join方法创建图片路径
tupian_path = os.path.join(dangqian_path, "tupian")
if not os.path.exists(tupian_path):  # 判断图片路径是否存在，若不存在就创建该路径
    os.mkdir(tupian_path)
for i in tag_image:
    #print(i["title"],i["data-original"])
    #下载图片
    r2 = requests.get(i["data-original"])
    #将图片内容写入某文件夹下，并以图片title命名
    #首先获取当前路径
    file_name = open(os.path.join(tupian_path, "%s.png"%i["title"]), "wb")
    file_name.write(r2.content)
    file_name.close()
