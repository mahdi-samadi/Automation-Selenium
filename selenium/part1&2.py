from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://google.com')

# driver.find_element('id', 'APjFqb').send_keys('wikipedia').click()
# sleep(3)
# window_title = driver.title
# print(window_title)
# sleep(1)
# driver.get('https://wikipedia.com')
# sleep(1)
# driver.back()
# sleep(1)
# driver.switch_to.new_window('window')
# sleep(2)
# driver.switch_to.new_window('tab')
# driver.get('https://yahoo.com')
# yahoo_window = driver.current_window_handle

# all_handle = driver.window_handles
# driver.switch_to.window(all_handle[0])
# sleep(1)

window_size = driver.get_window_size()
print(window_size)
driver.quit()