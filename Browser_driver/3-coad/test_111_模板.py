from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://tpshop-test.itheima.net/")

driver.find_element_by_class_name("red").click()
driver.find_element_by_class_name("text_cmu").send_keys("17485296311")
driver.find_element_by_css_selector("#password").send_keys("123456")
driver.find_element_by_css_selector("#verify_code").send_keys("8888")
driver.find_element_by_css_selector("[onclick='checkSubmit();']").click()

a = driver.find_element_by_css_selector("[class='layui-layer-content layui-layer-padding']").text
print("实际结果为%s" % a)

