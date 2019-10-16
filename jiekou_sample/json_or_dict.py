# -*- coding:utf-8 -*-
#发送带有JSON格式的参数

import json
import requests

url = "http://httpbin.org/post"

dict_value = {
    "姓名":"欧成",
    "年龄":30,
    "体重":"68公斤",
    "学历":"本科",
    "其他":["80","900","8300"]
}

#两种传JSON值的方法
# r1 = requests.post(url, json=dict_value)
r1 = requests.post(url, data=json.dumps(dict_value))
print(type(r1.text), r1.text)

# dict_change_json = json.dumps(dict_value)
# print(type(dict_change_json),dict_change_json)
#
# json_change_dict = json.loads(dict_change_json)
# print(type(json_change_dict),json_change_dict)