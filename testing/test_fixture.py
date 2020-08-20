# -*- coding:utf-8 -*-
import pytest
@pytest.fixture
def login():
    print("需要dengl ")
    username="hah"
    yield username
    print("teardown")
class TestDemo:
    # def setup_class(self):
    #     print("setup_class")
    # def teardown_class(self):
    #     print("teardown_class")
    # def setup(self):
    #     # 第一步，打开浏览器
    #     print("第一步，打开浏览器")
    # def teardown(self):
    #     # 第五步，关闭浏览器
    #     print("第五步，关闭浏览器")
    def test_a(self,login):

        #第二步，输入网址
        #第三步，定位
        #第四步，各种操作
        print("test_a")
        print(f"testa==={login}")
        # pass
    def test_b(self,login):
        print("test_b")
        # pass
    def test_c(self):
        print("test_c")
        pass
