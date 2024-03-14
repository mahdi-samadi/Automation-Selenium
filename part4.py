from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")

driver.find_element("xpath" , "//* [@id = 'male']")


sleep(3)