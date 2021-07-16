from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time
import pytest
# import grequest_throttle


# 谷歌
driver = webdriver.Chrome('/Users/out/Documents/testRepo/Browser_driver/chromedriver')
# 最大化窗口
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(5)

driver.get('https://shanghai.baixing.com/')

# action = ActionChains(driver)
# title = driver.title
# url = driver.current_url
# Edge莫名其妙报错-放弃
# driver = webdriver.Edge('/Users/out/Documents/testRepo/Browser_driver/MicrosoftWebDriver')




driver.find_element_by_xpath("//*[text()='[切换城市]']").click()
driver.find_element_by_xpath("//*[text()='上海']").click()
driver.find_element_by_xpath("//*[@placeholder='求职找房找服务']").send_keys('租房')
driver.find_element_by_xpath("//*[@title='搜索']").click()
driver.find_element_by_xpath("//*[text()='浦东新区']").click()
driver.find_element_by_css_selector("[name = '价格[0]']").send_keys(800)
driver.find_element_by_css_selector("[name = '价格[1]']").send_keys(2000)
driver.find_element_by_css_selector("[value = '筛选']").click()
driver.find_element_by_xpath("//select[1]").click()
driver.find_element_by_xpath("//option[text()='1室']").click()
time.sleep(0.5)
driver.find_element_by_xpath("//select[2]").click()
driver.find_element_by_xpath("//option[text()='东南']").click()
time.sleep(0.5)
driver.find_element_by_xpath("//select[3]").click()
driver.find_element_by_xpath("//option[text()='中']").click()
time.sleep(0.5)
# 伪元素::before 定位 https://blog.csdn.net/qq_38542085/article/details/78495350
# 弹出新窗口
driver.find_element_by_css_selector("i.icon-side-chat").click()
# 获取所有句柄
handles = driver.window_handles
# 句柄返回的列表最新的是-1
driver.switch_to.window(handles[-1])
print(driver.title)
time.sleep(1)

# driver.find_element_by_xpath("//*[text()='手机号不用如何换绑']").click()

a = driver.find_element_by_xpath("//*[contains(text(),'可以')]").text
print(f'你是谁：{a}')

time.sleep(3)
driver.quit()