"登录页面"

# 对象库层：基于测试用例找到该页面所有需要操作的元素对象，统一管理
from selenium.webdriver.common.by import By

from test_01 import Driver01


class LonginPage:  # 定义对象库层类

    def __init__(self):  # 初始化方法定义代表每个元素对象的实例属性
        # 定义驱动对象的实例属性
        self.driver = Driver01.get_driver()  # 调用驱动对象的方法复制给变量
        # 用户名输入框
        self.username = (By.ID,"username")
        # 密码输入框
        self.password = (By.ID,"password")
        # 验证码输入框
        self.yzm = (By.ID,"verify_code")
        # 登录按钮
        self.den = (By.NAME, "sbtbutton")

    # 找到用户名输入框
    def find_username(self):
        # return self.driver.find_element_by_id("username")
        # return self.driver.find_element(By.ID,"username")
        return self.driver.find_element(self.username[0],self.username[1])
        # return self.driver.find_element(*self.username)  拆包思想
    # 找到密码输入框
    def find_password(self):
        # return self.driver.find_element_by_id("password")
        # return self.driver.find_element(By.ID,"password")
        return self.driver.find_element(self.password[0], self.password[1])
    # 找到验证码输入框
    def find_yzm(self):
        # return self.driver.find_element_by_id("verify_code")
        # return self.driver.find_element(By.ID,"verify_code")
        return self.driver.find_element(self.yzm[0], self.yzm[1])
    # 找到登录输入框
    def find_den(self):
        # return self.driver.find_element_by_name("sbtbutton")
        # return self.driver.find_element(By.NAME, "sbtbutton")
        return self.driver.find_element(self.den[0], self.den[1])
# 定义操作层类：对于界面的每个元素都有自己的操作方法
class CaoZuo:

    def __init__(self):
        # 创建对象库层的实例化对象，把他赋值给变量
        self.pp = LonginPage()

    # 用户名输入框操作
    def input_username(self, use):  # 定义方法名
        # 清除文本
        self.pp.find_username().clear()
        # 实例化对象赋值的变量.获取的元素对象.元素操作
        self.pp.find_username().send_keys(use)

    # 密码输入框操作
    def input_password(self, pas):
        self.pp.find_password().clear()
        # 实例化对象赋值的变量.获取的元素对象.元素操作
        self.pp.find_password().send_keys(pas)

    # 验证码输入框操作
    def input_yzm(self, yzm):
        #清除文本
        self.pp.find_yzm().clear()
        # 实例化对象赋值的变量.获取的元素对象.元素操作
        self.pp.find_yzm().send_keys(yzm)

    # 登录按钮点击操作
    def click_den(self):
        # 实例化对象赋值的变量.获取的元素对象.元素操作
        self.pp.find_den().click()


# 业务层：连续调用多元素的操作方法形成完整的业务动作

class YeWu:  # 定义业务层的类

    # 创建操作层的实例化对象赋值给变量
    def __init__(self):
        self.qq = CaoZuo()

    # 登录操作
    # 调用操作层的方法
    def test_caozuo(self, use, pas, yzm):  #参数不要写死使用参数代替
        # 1.输入用户名
        self.qq.input_username(use)
        # 1.输入密码
        self.qq.input_password(pas)
        # 1.输入验证码
        self.qq.input_yzm(yzm)
        # 1.点击登录
        self.qq.click_den()

