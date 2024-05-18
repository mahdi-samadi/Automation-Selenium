from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(1)
alert = Alert(driver)
actions = ActionChains(driver)


# driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# 1) Get text
# driver.find_element(By.XPATH, '//button[text()="Click for JS Alert"]').click()
# print(alert.text)
# sleep(3)

# 2) Accept
# driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]').click()
# alert.accept()

# driver.find_element(By.XPATH, '//*[text()="You clicked: Ok"]')
# dom = driver.page_source
# assert 'You clicked: Ok' in dom
# print("pass")
# sleep(3)


# 3) Dismiss
# driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]').click()
# alert.dismiss()
# sleep(3)
# driver.find_element(By.XPATH, '//*[text()="You clicked: Cancel"]')
# dom = driver.page_source
# assert 'You clicked: Cancel' in dom
# print('success')
# sleep(3)



driver.get("https://material.angular.io/components/dialog/examples")

cdk_button = driver.find_element(By.XPATH, "//*[@class='mdc-button__label' and text()='CDK']")
offset = cdk_button.location
print('11111111111111111111111111111111111111')
driver.find_element(By.XPATH, '(//button[@class="mdc-button mat-mdc-button mat-unthemed mat-mdc-button-base"]//*[text()= "Open dialog"])[1]').click()
#validation
driver.find_element(By.XPATH, "//h3[text()= 'Develop across all platforms']")
driver.find_element(By.XPATH, '//button//*[text() = "Install"]')
driver.find_element(By.XPATH, '//button//*[text()= "Cancel"]')

actions.move_by_offset(offset['x'], offset['y']).pause(1).click().perform()
sleep(3)
driver.find_element(By.XPATH, '(//button[@class="mdc-button mat-mdc-button mat-unthemed mat-mdc-button-base"]//*[text()= "Open dialog"])[1]').click()
print('mahdi')