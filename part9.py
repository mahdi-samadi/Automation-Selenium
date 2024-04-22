from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.action_chains import ActionChains

service = ChromiumService
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://trytestingthis.netlify.app/")
driver.maximize_window()
sleep(5)

el = driver.find_element('xpath','//button[text()= "Double-click me"]')
actions.double_click(el).perform()

driver.find_element('xpath', "//*[text() = 'Your Sample Double Click worked!']")
sleep(2)