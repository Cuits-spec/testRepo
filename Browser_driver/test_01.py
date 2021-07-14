
import pytest


# 定义被测试的函数
def divide(x, y):
    a = x / y
    return a


# 1.定义pytest的测试类
class TestDivide:

    # 2.定义测试方法
    # 测试个数位的除法

    def test_pp_001(self):
        a = divide(2, 2)

        print("测试非0整数个位的除法")

        # 测试多位数的除法

    def test_pp_002(self):
        a = divide(20, 10)
        print("测试多位数的除法")