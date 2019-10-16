# -*- coding:utf-8 -*-
from urllib import parse
import re
a = "你好360公司，你是好员工公公"
#urlcode编码
bianma_value = parse.quote(a)
print(bianma_value)
#urlcode解码
jiema_value = parse.unquote(bianma_value)
print(jiema_value)
#正则表达式取：360
re_value = re.findall("好(.+?)公",a)
print(re_value)#列表
A = a.encode("GB2312")
print(A)
B = A.decode("GB2312")
print(B)