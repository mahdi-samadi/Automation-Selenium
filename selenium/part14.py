from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
user_dir = "E:/ALL Project/automationSelenium/selenium/user-dir"
options.add_argument(f"user-data-dir = {user_dir}")

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://app.clockify.me/en/signup")
driver.find_element(By.XPATH, "//input[@type ='email']").send_keys("mamal@gmail.com")