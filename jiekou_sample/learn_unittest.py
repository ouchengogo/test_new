import unittest
# help(unittest)
a = None
class testAdd(unittest.TestCase):
    def setUp(self):
        print("前提约束！我是setUp()")

    @classmethod
    def setUpClass(cls):
        print("前提约束，我是setUpClass(),但我只运行一次！")

    def testCase_001(self):#test开头
        print("第一条用例开始执行！")
        self.assertEqual((1 + 2), 3)
        self.assertEqual((2 + 5), 7)

    # @unittest.skip("跳过")#下一个用例跳过
    def testCase_002(self):#test开头
        print("第二条用例开始执行！")
        self.assertTrue(1==1)
        self.assertEqual((7 - 4), 3)

    def tearDown(self):
        print("用例执行完毕！")
        print("-------------------")

    @classmethod#不写这个下边的函数会报TypeError: tearDownClass() missing 1 required positional argument: 'cls'这个错误
    def tearDownClass(cls):
        print("全部用例执行完毕！我是tearDownClass！")

# class test_Add_1(unittest.TestCase):
#     def testCase_001(self):
#         print("第三条用例开始执行！")
#         print("-------------------")
#         self.assertTrue(1, 1)

if __name__ == "__main__":#注意写法：__name__ == "__main__"
    unittest.main()#unittest.main()