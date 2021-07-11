"""
断言知识点
"""
# 1.导包
import time
from selenium import webdriver


# 定义测试类
class TestLogin:

    def setup_class(self):
        # 2.创建浏览器驱动对象
        self.driver = webdriver.Chrome()
        # 3.窗口最大化
        self.driver.maximize_window()
        # 4.设置隐式等待
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        # 7.关闭浏览器
        time.sleep(2)
        self.driver.quit()

    # 函数级别初始化方法
    def setup(self):
        # 5.打开测试网址
        self.driver.get("http://tpshop-test.itheima.net/")

    # 函数级别销毁的方法
    def teardown(self):
        pass

    # 定义测试方法
    def test_password_error(self):
        # 6.执行登陆业务
        self.driver.find_element_by_class_name("red").click()
        self.driver.find_element_by_id("username").send_keys("15800000001")
        self.driver.find_element_by_id("password").send_keys("error")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_name("sbtbutton").click()
        msg = self.driver.find_element_by_css_selector(".layui-layer-content").text
        time.sleep(2)
        print("实际结果为{}".format(msg))
        # 断言,期望"密码不能为空!" == msg对比的结果为真
        assert msg == "密码不能为空!"

    def test_account_not_exist(self):
        # 6.执行登陆业务
        self.driver.find_element_by_class_name("red").click()
        self.driver.find_element_by_id("username").send_keys("15800001188")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_name("sbtbutton").click()
        msg = self.driver.find_element_by_css_selector(".layui-layer-content").text
        time.sleep(2)
        print("实际结果为{}".format(msg))
        # 断言,期望"账户不存在!" == msg对比的结果为真
        assert msg == "账号不存在!"
