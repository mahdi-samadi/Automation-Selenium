from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://wikipedia.com")

# 1 => ID
# el1 = driver.find_element('id', 'searchInput').send_keys('hello world!')

# 2 => xpath
# el2 = driver.find_element('xpath', '//input[@type="search"]').send_keys('hello world!')
# print(el1)
# print(el2)
# assert el1 == el2
# el3 = driver.find_element('xpath', '//*[text()="Italiano"]').click()

# 3 ==> tag
# el3 = driver.find_element('tag name', 'select').click()
# sleep(4)

# 4 ==> link text
# el4 = driver.find_element('link text', 'Download Wikipedia for Android or iOS').click()
# sleep(3)

# 5 => partial link text
# el5 = driver.find_element('partial link text', 'Download')

#6 ==> class name
# el6 = driver.find_element('class name', 'svg-search-icon').click()
# sleep(3)

#7 css selector
# el7 = driver.find_element('css selector', '.svg-search-icon').click()
# el8 = driver.find_element('css selector', '#searchInput').click()
# el8 = driver.find_element('css selector', 'body.jsl10n-visible:nth-child(2) main:nth-child(1) div.search-container:nth-child(3) form.pure-form fieldset:nth-child(1) > button.pure-button.pure-button-primary-progressive:nth-child(4)').click()
# sleep(3)