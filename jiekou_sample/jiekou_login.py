import requests
import time
import unittest

"""class test_login(unittest.TestCase):
    def setUp(self):
        pass

    def test_login(self):
        test_request = requests.post("http://127.0.0.1:1080/WebTours/index.htm", data = {"username":"jojo1","password":"bean"})
        result = test_request.status_code
        self.assertEqual(result, 200)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()"""
#登录禅道
'''login_value = {
    "account":"zhangcheng",
    "password":"1q2w3e4r5t",
    "referer":"/zentao/",
    "verifyRand":"511546094",
    "passwordStrength":"1"
}'''

login_value = {
    "account":"zhangcheng",
    "password":"1q2w3e4r5t",
    "referer":"/zentao/",
    "passwordStrength":"1"
}#passwordStrength为密码强度检测参数，0-密码弱；1-密码强。密码弱时就会跳转到'/zentao/my-changepassword.html'页面

header_value = {
    "Authorization":"Basic emVudGFvOjEyMzQ1Ng=="
}#解决提示401 Unauthorized

login_request = requests.post("http://127.0.0.1:8080/zentao/user-login-L3plbnRhby8=.html", headers=header_value, data=login_value)
login_cookie = login_request.cookies
#查看个人bug
bug_request = requests.get("http://127.0.0.1:8080/zentao/my-bug.html", cookies=login_cookie, headers=header_value)#没有cookies就会跳转到/zentao/user-login-L3plbnRhby9teS1idWcuaHRtbA==.html
#print("--------------")
print(bug_request.text)
#print("--------------")