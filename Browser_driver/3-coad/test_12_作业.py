import time

import pytest
from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# 测试TPshop登录
class TestLogin:
    a = 2

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://tpshop-test.itheima.net/")

    def setup(self):
        time.sleep(3)
        self.driver.get("http://tpshop-test.itheima.net/")

    def teardown_class(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.run(order=3)
    def test_login(self):
        self.driver.find_element_by_class_name("red").click()
        self.driver.find_element_by_id("username").send_keys("15800000001")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_name("sbtbutton").click()

    @pytest.mark.run(order=2)
    @pytest.mark.skipif(a>1,reason="想跳就跳")
    def test_login_no_password(self):
        self.driver.find_element_by_class_name("red").click()
        self.driver.find_element_by_id("username").send_keys("15800000001")
        self.driver.find_element_by_id("password").send_keys("")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_name("sbtbutton").click()
    @pytest.mark.run(order = 1)
    def test_login_no_account(self):
        self.driver.find_element_by_class_name("red").click()
        self.driver.find_element_by_id("username").send_keys("")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_name("sbtbutton").click()

