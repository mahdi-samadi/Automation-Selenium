from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep


base_url = "https://play1.automationcamp.ir"
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(f"{base_url}/forms.html")
driver.find_element('id','check_python').click()
check1 = driver.find_element('id', 'check_validate').text
assert check1 == "PYTHON"
text2 = "hello mahdi"
driver.find_element('id', 'notes').send_keys(text2)
check2 = driver.find_element('id','area_notes_validate').text
assert check2 == text2
sleep(10)



 