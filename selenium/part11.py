from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service= service)
driver.maximize_window()
driver.implicitly_wait(2)

#1 - 'By' Class
# driver.find_element(By.XPATH)
# driver.find_element(By.ID)

#2 - Get Text
# driver.get("https://material.angular.io/")
# el = driver.find_element(By.CLASS_NAME, 'mat-mdc-button-touch-target')
# attr = el.text
# print(attr)

#3 - Get Link, Class, ID, ...
# el = driver.find_element(By.XPATH, "//*[@class = 'mdc-button__label' and text() = 'Components' ]" ).click()
# attr = el.__getattribute__('class')
# print(attr)
# assert 'selected' in attr, 'Element is not selected'
# el2 = driver.find_element(By.XPATH, "//*[@class = 'mdc-button__label' and text() = 'Components' ]/.." ).click()
# sleep(1)
# attr2 = el.__getattribute__('class')
# assert 'selected' not in attr2, 'Element is selected'
# print(attr2)
# sleep(2)


#4 - Radio Button
driver.get("https://material.angular.io/components/radio/examples")
el = driver.find_element(By.ID, 'mat-radio-2')
attr1 = el.get_attribute('class')
assert 'checked' not in attr1
el.click()
attr2 = el.get_attribute('class')
# assert 'checked' in attr2
sleep(3)