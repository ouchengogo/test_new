from bs4 import BeautifulSoup
import requests
r1 = requests.get("http://699pic.com/nature.html")
soup = BeautifulSoup(r1.text, "html.parser")
li_tag = soup.li
print(li_tag)#li中还有儿子a
print(li_tag.a)#a中还有儿子i,span.如何区分是儿子还是孙子，看层级就可以，比如用浏览器打开
print(li_tag.a.i, "\n", li_tag.a.span)
#关于li_tag的属性
print(li_tag["class"], "\n", li_tag["a"])#li_tag["a"]这个是错误的，只有在<li XXXXXX>中才叫属性