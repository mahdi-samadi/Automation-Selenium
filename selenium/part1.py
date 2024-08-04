from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


base_url = "https://testautomation-playground.herokuapp.com/"
driver = webdriver.Chrome()

# driver.get('https://google.com')
# # driver.find_element_by_name('q').click()
# search_field = driver.find_element('name', 'q')
# search_field.send_keys("keep it simple stupid")
# search_field.send_keys(Keys.RETURN)


driver.get(f"{base_url}/forms.html")
driver.find_element('id', 'check_python').click()
check1 = driver.find_element('id', 'check_validate').text
assert check1 == "PYTHON"
text1 = "Hello Automation World!"
driver.find_element('id', 'notes').send_keys(text1)
check2 = driver.find_element('id', 'area_notes_validate').text
assert check2 == text1









# driver.get(f"{base_url}/forms.html")
# driver.find_element('id','check_python').click()
# check1 = driver.find_element('id', 'check_validate').text
# assert check1 == "PYTHON"
# text2 = "hello mahdi"
# driver.find_element('id', 'notes').send_keys(text2)
# check2 = driver.find_element('id','area_notes_validate').text
# assert check2 == text2
# sleep(10)



 