from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(2)

# 5 - wait until element is enabled
# def wait_until_element_is_enabled(selector, locator, timeout):
#   for i in range(timeout*2):
#     try:
#       el = driver.find_element(selector, locator)
#       assert el.is_enabled()
#       return
#     except:
#       sleep(0.5)

# # 6 - wait until element is not enabled
# def wait_until_element_is_not_enabled(selector, locator, timeout):
#   for i in range(timeout*2):
#     try:
#       el = driver.find_element(selector, locator)
#       assert not el.is_enabled()
#       return
#     except:
#       sleep(0.5)

# driver.get("https://play1.automationcamp.ir/expected_conditions.html")
# trigger = driver.find_element(By.ID, "enabled_trigger")
# trigger.location_once_scrolled_into_view
# trigger.click()
# wait_until_element_is_enabled(By.ID, 'enabled_target', 5)
# print('mahdi')


# 7- wait until element is visible
def wait_until_element_is_visible(selector, locator, timeout=5):
  for i in range(timeout * 2):
    try:
      el = driver.find_element(selector, locator)
      assert el.is_displayed()
      return
    except:
      sleep(0.5)

# 8- wait until element is visible
def wait_until_element_is_not_visible(selector, locator, timeout=5):
  for i in range(timeout * 2):
    try:
      el = driver.find_element(selector, locator)
      assert el.is_displayed()
      return
    except:
      sleep(.5)

driver.get('https://play1.automationcamp.ir/expected_conditions.html')
trigger = driver.find_element(By.ID, "visibility_trigger")
trigger.location_once_scrolled_into_view
print(driver.find_element(By.ID, "visibility_target").is_displayed())
trigger.click()
wait_until_element_is_visible(By.ID, "visibility_target")
print(driver.find_element(By.ID, "visibility_target").is_displayed())
