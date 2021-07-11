"""
断言知识点
"""
# 1.导包
import time

import pytest

from test_01 import Driver01, get_case_data
from test_01 import get_test
from test_022 import YeWu


# 定义测试类
class TestLogin:

    def setup_class(self):
        # 创建的浏览器驱动对象
        self.driver = Driver01.get_driver()
        # 登录页面业务层的对象
        self.kk = YeWu()

    def teardown_class(self):
        # 7.关闭浏览器
        Driver01.driver_quit()

    # 函数级别初始化方法
    def setup(self):
        # 5.打开测试网址
        self.driver.get("http://tpshop-test.itheima.net/")

    # 函数级别销毁的方法
    def teardown(self):
        pass

    list1 = [("15800000001", "error", "8888", "密码错误!"), ("15800000021", "123456", "8888", "账号不存在!")]

    @pytest.mark.parametrize(("username", "password", "yzm", "sjjg"),(get_case_data("../data/login_case.json")))

    def test_login(self, username, password, yzm, sjjg):
        self.driver.find_element_by_class_name("red").click()
        self.kk.test_caozuo(username, password, yzm)
        a = get_test("//*[@class='layui-layer-content layui-layer-padding']")
        assert a == sjjg

    # # 定义测试方法
    # def test_password_error(self):
    #     # 6.执行登陆业务
    #     self.driver.find_element_by_class_name("red").click()
    #
    #     self.kk.test_caozuo("15800000001", "error", "8888")
    #
    #     a = get_test("//*[@class='layui-layer-content layui-layer-padding']")
    #     # 断言,期望"密码不能为空!" == msg对比的结果为真
    #     # print("实际结果为{}".format(a))
    #     assert a == "密码错误!"
    #
    # def test_account_not_exist(self):
    #     # 6.执行登陆业务
    #     self.driver.find_element_by_class_name("red").click()
    #
    #     self.kk.test_caozuo("15800000021", "123456", "8888")
    #
    #     a = get_test("//*[@class='layui-layer-content layui-layer-padding']")
    #     # time.sleep(2)
    #     # print("实际结果为{}".format(a))
    #     # # 断言,期望"账户不存在!" == msg对比的结果为真
    #     assert a == "账号不存在!"
