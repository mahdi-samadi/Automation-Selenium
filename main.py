from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://google.com")

driver.find_element('name', 'q').send_keys('mahdisamadi')