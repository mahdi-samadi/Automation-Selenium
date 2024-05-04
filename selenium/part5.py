from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")

driver.find_element("xpath" , "//*[contains(text(), 'layout two)]")
driver.find_element("xpath" , "//*[contains(@id, 'lna)]")
driver.find_element("xpath" , "//*[starts-width(@id, 'lna)]")
driver.find_element("xpath" , "//tbody//tr[position()=2]")   
driver.find_element("xpath" , "//tbody//tr[2]")
driver.find_element("xpath" , "//tbody//tr[last() - 1]")      #todo yeki monde be akhar
driver.find_element("xpath" , "//tbody[count(.//tr) = 7]")   #todo hatman bayad . qeyd shavad ta dar kolle html be donbalehs nagarde va az tbody be bado bgarde.
driver.find_element("xpath" , "//*[normalize-space( text() ) = 'Option 1']")
driver.find_element["xpath" , "//*[translate (@value, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' , 'abcdefghijklmnopqrstuvwxyz') = 'Option 1']"]
driver.find_element["xpath" , "//*[normalize-space(translate (@value, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' , 'abcdefghijklmnopqrstuvwxyz') = 'Option 1')]"]
driver.find_element["xpath" , "//*[string-length(@id) = 4]"]
driver.find_element["xpath" , "//*[round (text()) = '430']"]
driver.find_element["xpath" , "//*[floor (text()) = '430']"]  # addad ro asharesho dar nazar nmigire
driver.find_element["xpath" , "//*[@type = 'radio' and not (@id = 'male')]"]
driver.find_element["xpath" , "//*[substring-before (text() , ':') = 'Username]"]

sleep(3)