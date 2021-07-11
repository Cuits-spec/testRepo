"""
断言知识点
"""
# 1.导包
import time

import pytest
from selenium import webdriver


# 定义测试类
from testCase_kaos.kaos03 import YeWu
from testCase_kaos.kaos_page import get_test, get_case_data, Driver_001


class TestLogin:

    def setup_class(self):
        # 2.创建浏览器驱动对象
        self.driver = Driver_001.get_driver()
        self.kk = YeWu
    def teardown_class(self):
        # 7.关闭浏览器
        time.sleep(2)
        self.driver.quit()

    # 函数级别初始化方法
    def setup(self):
        # 5.打开测试网址
        self.driver.get("http://tpshop-test.itheima.net/Admin/Admin/login")

    # 函数级别销毁的方法
    def teardown(self):
        pass

    # 定义测试方法
    @pytest.mark.parametrize(("uesrname", "password", "yzm", "sjjg"),
                             get_case_data("../data/laos_case.json"))
    def test_001(self,uesrname,password,yzm,sjjg):

        self.driver.find_element_by_name("ssubmit").click()

        a = get_test("//*[contains(text(),'密码')]")
        assert a == sjjg

