import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get(
    "https://www.xyz.cn/")
# driver.find_element_by_link_text("旅游险").click()
# handles = driver.window_handles
# driver.switch_to.window(handles[-1])
# a = driver.find_element_by_css_selector(".pro_all_products").text
# print("实际结果是%s" % a)


# action = ActionChains(driver)
# action.move_to_element(driver.find_element_by_link_text("旅游险"))
# driver.find_element_by_link_text("国内旅行保险").click()
# handles = driver.window_handles
# driver.switch_to.window(handles[-1])
# driver.find_element_by_css_selector(".pro_all_products").click()
# a = driver.find_element_by_css_selector(".pro_all_products").text
# print("结果是%s" % a)


# driver.find_element_by_css_selector("#keyword").send_keys("健康险")
# driver.find_element_by_css_selector("#subSearch").click()
# c = driver.find_element_by_css_selector(".hazardC_tit_h1").text
# print("%s" % c)

driver.find_element_by_css_selector("#keyword").send_keys("健康险")
driver.find_element_by_css_selector("#subSearch").click()
driver.find_element_by_xpath("//li/*[text()='产责险']").click()
# time.sleep(2)
# d = driver.find_element_by_css_selector("div>.pro_all_products").text
# print("%s" % d)

# time.sleep(3)
# driver.quit()
