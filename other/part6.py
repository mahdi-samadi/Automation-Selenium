from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")

# parent
driver.find_element("xpath" , "//*[@id = 'uname']/parent::*[@id = 'def']")

# ancestor
driver.find_element("xpath" , "//td[text() = 'Singer']/ancestor::table[@style = 'width:100%']")

# ham dar parent ham dar khudesh
driver.find_element("xpath" , "//tbody/tr[3]/child::*[text()= 'Singer']")

# gashtan dar tamame zire mojmoe haye parent (noqte moqabele ancestor)
driver.find_element("xpath" , "//table/descendant::*[text() = 'Singer']")
driver.find_element("xpath" , "//table//*[text() = 'Singer']")

#radyabi dar element haye ham javar:
driver.find_element("xpath" , "//select[@id = 'option']/following::*[@value = 'option']")

# element haye ham sath (sibling) dar yek level hastan(yani age ye id ro peyda kard ba sibling azon be bado miare):
driver.find_element("xpath" , "//select[@id = 'option']/following-sibling::*[@value = 'option']")

# element hayei ke qable on elemneti ke peyda mikonim bahsan
driver.find_element("xpath" , "//select[@id = 'optionx']/preceding::*[@value = 'option 2']")

# element haye ham javare khudesh ke qabl az khudesh hastan:
driver.find_element("xpath" , "//*[@id = 'abcd1234']/preceding-sibling::*[@value = 'option 2']")
