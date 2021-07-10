# 如何编写一个pytest的测试类？
import pytest


# 定义被测试的函数
def divide(x, y):
    a = x / y
    return a


# 1.定义pytest的测试类
@pytest.mark.run(order=3)    #让他在第三次调用
class TestDivide:

    # 2.定义测试方法
    # 测试个数位的除法

    def test_pp_001(self):
        a = divide(1, 2)
        print("用了排序使我本来是第一个现在变成第三个的个位除法")

        # 测试多位数的除法

    def test_pp_002(self):
        a = divide(20, 10)
        print("用了排序使我本来是第一个现在变成第三个的多位除法")
