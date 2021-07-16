import time
# import pytest
from selenium import webdriver


# 创建测试类
class Testchrome:

    # 创建方法级别的前置条件
    def setup(self):
        self.driver = webdriver.Chrome('/Users/out/Documents/testRepo/Browser_driver/chromedriver')  # 创建驱动对象
        self.driver.maximize_window()  # 最大化窗口
        self.driver.implicitly_wait(5)  # 隐式等待
        self.driver.get('https://shanghai.baixing.com/')

    # 创建方法级别的后置条件
    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_001(self):
        print("111")
        self.driver.find_element_by_xpath("//*[text()='[切换城市]']").click()
        self.driver.find_element_by_xpath("//*[text()='上海']").click()
        self.driver.find_element_by_xpath("//*[@placeholder='求职找房找服务']").send_keys('租房')
        self.driver.find_element_by_xpath("//*[@title='搜索']").click()
        self.driver.find_element_by_xpath("//*[text()='浦东新区']").click()
        self.driver.find_element_by_css_selector("[name = '价格[0]']").send_keys(800)
        self.driver.find_element_by_css_selector("[name = '价格[1]']").send_keys(2000)
        self.driver.find_element_by_css_selector("[value = '筛选']").click()
        q = self.driver.find_element_by_xpath("//*[text()='800-2000元']").text
        print(f'筛选结果为：{q}')

    def test_002(self):
        self.test_001()
        self.driver.find_element_by_xpath("//select[1]").click()
        self.driver.find_element_by_xpath("//option[text()='1室']").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//select[2]").click()
        self.driver.find_element_by_xpath("//option[text()='东南']").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//select[3]").click()
        self.driver.find_element_by_xpath("//option[text()='中']").click()
        time.sleep(0.5)
        # 伪元素::before 定位 https://blog.csdn.net/qq_38542085/article/details/78495350
        self.driver.find_element_by_css_selector("i.icon-side-chat").click()
        a = self.driver.find_element_by_xpath("//*[contains(text(),'交易')]").text
        print(f'实际结果是：{a}')

    def test_003(self):
        self.test_001()
        self.test_002()
        self.driver.find_element_by_xpath("//*[contains(text(),'对应账户')]").click()
        self.driver.find_element_by_xpath("//*[contains(text(),'对应账户')]").send_keys('哈哈哈')
        c = self.driver.find_element_by_xpath("//*[contains(text(),'哈哈')]").text
        print(f'发送的是：{c}')

print(11)
