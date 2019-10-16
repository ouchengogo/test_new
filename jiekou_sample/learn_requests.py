import requests
import time

s = requests.session()#定义微型浏览器，后续请求通过它实现

login_value = {
    "account":"zhangcheng",
    "password":"1q2w3e4r5t",
    "referer":"/zentao/",
    "passwordStrength":"1"
}#passwordStrength为密码强度检测参数，0-密码弱；1-密码强。密码弱时就会跳转到'/zentao/my-changepassword.html'页面

header_value = {
    "Authorization":"Basic emVudGFvOjEyMzQ1Ng=="
}#解决提示401 Unauthorized


#登录
login_request = s.post("http://127.0.0.1:8080/zentao/user-login-L3plbnRhby8=.html", headers=header_value, data=login_value)
#login_cookie = login_request.cookies



#查看个人bug
bug_request = s.get("http://127.0.0.1:8080/zentao/my-bug.html", headers=header_value)#没有cookies就会跳转到/zentao/user-login-L3plbnRhby9teS1idWcuaHRtbA==.html
#print("--------------")
#print(bug_request.cookies)
#print("--------------")
#打开新增产品页面
open_product = s.get("http://127.0.0.1:8080/zentao/product-create.html", headers=header_value)
#print(open_product.cookies)
print("----------------------------------------------------------------------------------------------------------")
print(open_product.text)
print("----------------------------------------------------------------------------------------------------------")



#提交新增产品
uid_value_1 = input("输入uid:")
time.sleep(3)
body_value = {
    "name":"test_015",
    "code":"9978",
    "line":"0",
    "PO":"lixl",
    "QD":"lixl",
    "RD":"zhangcheng",
    "type":"normal",
    "status":"normal",
    "desc":"123466758910093",
    "acl":"private",
    "uid":uid_value_1
}
product_request = s.post("http://127.0.0.1:8080/zentao/product-create.html", headers=header_value, data=body_value)
print("******************************************")
print(product_request.text)
print("******************************************")
#打开新需求页面
open_xuqiu_request = s.get("http://127.0.0.1:8080/zentao/story-create-5-0-0.html", headers=header_value)
print(open_xuqiu_request.text)

#更新cookie
#设置cookies
# cookies_value = requests.cookies.RequestsCookieJar()
# cookies_value.set("preBranch","0")
# cookies_value.set("preProductID","5")
# cookies_value.set("storyModule","0")
# cookies_value.set("lastProduct","5")
# cookies_value.set("productStoryOrder","id_desc")
# cookies_value.set("windowWidth","1366")
# cookies_value.set("windowHeight","625")
# cookies_value.set("csrftoken","g2IM9Qtjh5I4AIfcuL8TbPOd7cSQ3oaUbmrTU4tffLidLIwhrfzSa5SnYzq1THWE")
# cookies_value.set("zentaosid","tnl30d3u1ml1etsabn82hkok03")
# #更新cookie
# s.cookies.update(cookies_value)

#提交新需求
header_value_2 = {
    "Authorization":"Basic emVudGFvOjEyMzQ1Ng==",
    "content-type":"multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
}
uid_value_2 = input("输入uid:")
time.sleep(3)
# xuqiu_body = {
#     "product":(None, "5"),
#     "module":(None, "0"),
#     "plan":"",
#     "source":(None, "customer"),
#     "sourceNote":"",
#     "assignedTo":(None, "lixl"),
#     "title":(None, "提需求_014"),
#     "color":"",
#     "pri":(None, "3"),
#     "estimate":"",
#     "spec":(None, "提需123456_014"),
#     "verify":(None, "啊啊_014"),
#     "status":(None, "draft"),
#     "labels[]":"",
#     "files[]":"",
#     "mailto[]":"",
#     "keywords":"",
#     "uid":(None, uid_value_2)
# }

xuqiu_body = {
    "product":"5",
    "module":"0",
    "plan":"",
    "source":"customer",
    "sourceNote":"",
    "assignedTo":"lixl",
    "title":"提需求_015",
    "color":"",
    "pri":"3",
    "estimate":"",
    "spec":"提需123456_015",
    "verify":"啊啊_015",
    "status":"draft",
    "labels[]":"",
    "files[]":"",
    "mailto[]":"",
    "keywords":"",
    "uid":uid_value_2
}

creat_request = s.post("http://127.0.0.1:8080/zentao/story-create-5-0-0.html", headers = header_value, data = xuqiu_body)
print("--------------------------------------------------")
print(creat_request.text)
print("--------------------------------------------------")
