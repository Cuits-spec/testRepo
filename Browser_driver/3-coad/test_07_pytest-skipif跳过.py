# 如何编写一个pytest的测试类？
import time

import pytest


# 定义被测试的函数
def divide(x, y):
    a = x / y
    return a


# 1.定义pytest的测试类
class TestDivide:

    a = 2
    # 2.定义测试方法
    # 测试个数位的除法



    @pytest.mark.skipif(a>1,reason="想跳就跳")   #当skipif里第一个参数为真的时候就跳过，第二个是跳过原因
    def test_pp_001(self):
        a = divide(2, 2)
        print("我是测试个位的除法")



        # 测试多位数的除法
    def test_pp_002(self):
        a = divide(20, 10)
        print("我是测试多位数的除法")
