import time

from selenium import webdriver


class TestCase:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.xyz.cn/")

    def teardown(self):
        time.sleep(2)
        self.driver.quit()


    def test_001(self):
        self.driver.find_element_by_link_text("旅游险").click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        a = self.driver.find_element_by_css_selector(".pro_all_products").text
        print("%s" % a)
        assert a == "共65个产品"

    def test_002(self):
        self.driver.find_element_by_link_text("国内旅行保险").click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.find_element_by_css_selector(".pro_all_products").click()
        b = self.driver.find_element_by_css_selector(".pro_all_products").text
        print("%s" % b)
        assert b == "共31个产品"

    def test_003(self):
        self.driver.find_element_by_css_selector("#keyword").send_keys("健康险")
        self.driver.find_element_by_css_selector("#subSearch").click()
        c = self.driver.find_element_by_css_selector(".hazardC_tit_h1").text
        print("%s" % c)
        assert c == "相关“健康险”保险产品"


