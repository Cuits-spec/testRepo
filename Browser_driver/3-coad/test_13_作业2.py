import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get(
    "https://www.xyz.cn/p/prodlist.do?xcase=viewSearchList&queryType=1&searchType=keyword&searchValue=%25E5%2581%25A5%25E5%25BA%25B7%25E9%2599%25A9")
driver.find_element_by_css_selector("[role='loginFromTopBar']").click()
handles = driver.window_handles
driver.switch_to.window(handles[-1])
driver.find_elements_by_xpath("//*[text()='账号登录']").clear()
driver.find_element_by_css_selector("#username").send_keys("13140017244")
driver.find_element_by_css_selector("#input2").send_keys("147258")
driver.find_element_by_css_selector("#defaultLogin").clear()


time.sleep(2)
driver.quit()