# -*- coding:utf-8 -*-
import requests

# url = "http://apis.juhe.cn/voiceRubbish/search"
url_2 = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"

# body_value = {
#     "q":"小龙虾",
#     "type":"2",
#     "key":"24da38d1774902964d326f12dcacee89"
# }
#
# r1 = requests.post(url, body_value)
# response_value = r1.text#str
# print(type(response_value),response_value)
# response_value = eval(response_value)#dict
# print(type(response_value), response_value)

r2 = requests.get(url_2)
print(type(r2.json()))
a = r2.json()["rank"]
print(a)
