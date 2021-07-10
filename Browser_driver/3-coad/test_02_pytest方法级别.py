# 如何编写一个pytest的测试类？
import time

import pytest


# 定义被测试的函数
def divide(x, y):
    a = x / y
    return a


# 1.定义pytest的测试类
class TestDivide:

    # 2.定义测试方法
    # 测试个数位的除法

    def setup(self):
        print("开始时间=%s" % (time.strftime("%H%M%S")))

    def teardown(self):
        print("结束时间=%s" % (time.strftime("%H%M%S")))

    def test_pp_001(self):
        a = divide(2, 2)
        print("我是测试个位的除法")

        # 测试多位数的除法

    def test_pp_002(self):
        a = divide(20, 10)
        print("我是测试多位数的除法")
