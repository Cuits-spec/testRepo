from selenium.webdriver.common.by import By
from test_03_zz1 import Qztj

class Duix:  # 定义对象库层类


    def __init__(self):

        self.lvyou01 = (By.LINK_TEXT,"旅游险")
        self.lvyou02 = (By.LINK_TEXT,"国内旅行保险")
        self.lvyou03 = (By.CSS_SELECTOR,"#keyword")


    def find_yiji(self):
        # return Qztj.get_driver().find_element_by_link_text("旅游险")
        return Qztj.get_driver().find_element(self.lvyou01[0],self.lvyou01[1])

    def find_sanji(self):

        return Qztj.get_driver().find_element(self.lvyou02[0],self.lvyou02[1])

    def find_sous(self):

        return Qztj.get_driver().find_element(self.lvyou03[0],[1])


class CaoZuo:

    def __init__(self):
        self.dd = Duix()


    def caozuo_lvyou01(self):
        self.dd.find_yiji().click()

    def caozuo_lvyou02(self):
        self.dd.find_sanji().click()

    def caozuo_lvyou03(self,cz):
        self.dd.find_sous().send_keys(cz)


class YeWu:

    def __init__(self):

        self.yy = CaoZuo()

    def test_01(self):
        self.yy.caozuo_lvyou01()

    def test_02(self):
        self.yy.caozuo_lvyou02()

    def test_03(self,cz):
        self.yy.caozuo_lvyou03(cz)
