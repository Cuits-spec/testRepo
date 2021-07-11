
from selenium.webdriver.common.by import By

from test_08_premise import Premise

#定义对象层
class My_object:


    def __init__(self):
        self.driver = Premise().method_01()

        self.use = (By.ID,"username")
        self.pas = (By.ID,"password")
        self.yzm = (By.ID,"verify_code")
        self.cck = (By.NAME,"sbtbutton")

    def username(self):
        return self.driver.find_element(self.use[0],self.use[1])

    def password(self):
        return self.driver.find_element(self.pas[0],self.pas[1])

    def verify(self):
        return self.driver.find_element(self.yzm[0],self.yzm[1])

    def my_click(self):
        return self.driver.find_element(self.cck[0],self.cck[1])


#操作层
class Operate:

    def __init__(self):
        self.caozuo = My_object()

    def look_user(self,use):
        self.caozuo.username().send_keys(use)

    def look_pass(self,pas):
        self.caozuo.password().send_keys(pas)

    def look_verify(self,yzm):
        self.caozuo.verify().send_keys(yzm)

    def look_click(self):
        self.caozuo.my_click().click()


#业务层
class Business:

    def __init__(self):
        self.bus = Operate()

    def haha(self,use,pas,yzm):
        self.bus.look_user(use)
        self.bus.look_pass(pas)
        self.bus.look_verify(yzm)
        self.bus.look_click()

