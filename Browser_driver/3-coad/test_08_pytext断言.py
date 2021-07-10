# 导包
import time

from selenium import webdriver



#定义pytest的测试类
class TestLogin:

    # 定义方法级别的前置条件
    def setup(self):
        self.driver = webdriver.Chrome()  ##创建驱动对象
        self.driver.maximize_window()   #最大化窗口
        self.driver.implicitly_wait(10)  # 隐式等待
        self.driver.get("http://tpshop-test.itheima.net/")  #打开地址

    # 方法级别的后置条件
    def teardown(self):
        time.sleep(2)
        self.driver.quit()


    def test_001(self):

        self.driver.find_element_by_class_name("red").click()
        self.driver.find_element_by_class_name("text_cmu").send_keys("17596565252")
        self.driver.find_element_by_css_selector("#password").send_keys()
        self.driver.find_element_by_css_selector("#verify_code").send_keys("8888")
        self.driver.find_element_by_css_selector("[onclick='checkSubmit();']").click()
        #打印结果
        a = self.driver.find_element_by_css_selector("[class='layui-layer-content layui-layer-padding']").text
        print("实际结果为%s" % a)
        assert a == "密码不能为空"   # 期望“密码不能为空”==a对比的结果为真

    def test_002(self):
        self.driver.find_element_by_class_name("red").click()
        self.driver.find_element_by_class_name("text_cmu").send_keys("17596565247")
        self.driver.find_element_by_css_selector("#password").send_keys("123456")
        self.driver.find_element_by_css_selector("#verify_code").send_keys("8888")
        self.driver.find_element_by_css_selector("[onclick='checkSubmit();']").click()
        #打印结果
        a = self.driver.find_element_by_css_selector("[class='layui-layer-content layui-layer-padding']").text
        print("实际结果为%s" % a)

