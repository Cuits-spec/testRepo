# 如何编写一个pytest的测试类？
import pytest


# 定义被测试的函数
from parameterized import parameterized


def divide(x, y):
    a = x / y
    return a


# 1.定义pytest的测试类
class TestDivide:

    # 2.定义测试方法
    # 测试个数位的除法

    def test_pp_001(self):
        a = divide(2, 2)
        assert a == 1

        # 测试多位数的除法

    def test_pp_002(self):
        a = divide(20, 10)
        assert a == 2


    @pytest.mark.parametrize(("x","y","z"),[(2,2,1),(20,10,2)])
    def canshuhua001(self,x,y,z):
        a = divide(x,y)
        assert a == z



    # def test_canshuhua(self):
    #     for x,y,z in [(2,2,1),(20,10,2)]:
    #         print("x=%d y=%d z=%d" % (x,y,z))
    #
    #         a = divide(x,y)
    #         assert a == z
    # #
    # @parameterized.expand([(2,2,1),(20,10,2)])
    # def canshuhua2(self,x,y,z):
    #     a = divide(x,y)
    #     assert a == z

