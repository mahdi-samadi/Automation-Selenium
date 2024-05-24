from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 2 switch to parent frame (Defualt content)
driver.get('https://www.python.org/dev/peps/')
sleep(2)
driver.switch_to.frame()