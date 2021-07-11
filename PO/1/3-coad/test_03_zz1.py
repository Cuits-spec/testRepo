import time

from selenium import webdriver

class Qztj:  #定义前置类

    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)

        return cls.__driver

    @classmethod
    def get_quit(cls):
        if cls.__driver is not None:
            time.sleep(2)
            cls.__driver.quit()
            cls.__driver = None




def get_test(css):
    a = Qztj.get_driver().find_element_by_css_selector(css).text
    time.sleep(2)
    print("%s" % a)

    return a





