#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
#打开文件，记住encoding
file_name = open("new 2.html", encoding='utf-8')
#获取soup对象
soup = BeautifulSoup(file_name, "html.parser")
#获取title的标签
title_tag = soup.title
#打印title的字符串内容
print("打印title字符串内容：",title_tag.string)
#获取iss的标签
is_tag = soup.iss
#打印iss的注释内容
print("打印iss的注释：",is_tag.string)
#获取script的tag对象
script_tag = soup.script
#打印script属性
print(script_tag.attrs)
print(script_tag["iss"])
print("-----------")
print(type(soup.body))
body_value = soup.body
print("-----------")
print(type(body_value.get_text()))
print("-----------")
#获取所有名称为link的标签
link_all_tag = soup.find_all("link")
for i in link_all_tag:
    print(i)
    print(i.attrs)#打印标签i的所有属性
    print("*******")