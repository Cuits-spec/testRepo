
from selenium.webdriver.common.by import By

from testCase_kaos import kaos_page
from testCase_kaos.kaos_page import Driver_001

class LonginPage:  # 定义对象库层类

    def __init__(self):
        self.driver = Driver_001.get_driver()  # 调用驱动对象的方法复制给变量
        self.username = (By.NAME,"username")
        self.password = (By.NAME,"password")
        self.yzm = (By.NAME,"vertify")
        self.den = (By.NAME, "ssubmit")
    # 找到用户名输入框
    def find_username(self):
        return self.driver.find_element(self.username[0],self.username[1])
    # 找到密码输入框
    def find_password(self):
        return self.driver.find_element(self.password[0], self.password[1])
    # 找到验证码输入框
    def find_yzm(self):
        return self.driver.find_element(self.yzm[0], self.yzm[1])
    # 找到登录输入框
    def find_den(self):
        return self.driver.find_element(self.den[0], self.den[1])
# 定义操作层类
class CaoZuo:
    def __init__(self):
        # 创建对象库层的实例化对象，把他赋值给变量
        self.pp = LonginPage()
    # 用户名输入框操作
    def input_username(self, use):
        # 清除文本
        self.pp.find_username().clear()
        self.pp.find_username().send_keys(use)
    # 密码输入框操作
    def input_password(self, pas):
        self.pp.find_password().clear()
        self.pp.find_password().send_keys(pas)
    # 验证码输入框操作
    def input_yzm(self, yzm):
        self.pp.find_yzm().clear()
        self.pp.find_yzm().send_keys(yzm)
   # 登录按钮点击操作
    def click_den(self):
        self.pp.find_den().click()
class YeWu:  # 定义业务层的类
    # 创建操作层的实例化对象赋值给变量
    def __init__(self):
        self.qq = CaoZuo()
    # 登录操作
    # 调用操作层的方法
    def test_caozuo(self, use, pas, yzm):
        # 1.输入用户名
        self.qq.input_username(use)
        # 1.输入密码
        self.qq.input_password(pas)
        # 1.输入验证码
        self.qq.input_yzm(yzm)
        # 1.点击登录
        self.qq.click_den()

