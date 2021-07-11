import time

from selenium import webdriver


#定义前置条件类
class Premise:

    def method_01(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        return self.driver


    def method_02(self):
        time.sleep(2)
        self.driver.quit()



