from pages.login import login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pages.mainPage import mainPage
import unittest


class LoginTests(unittest.TestCase)
driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait(3) # yani ta 3 saniye vasta ta amaliyat anjam beshe age 1 saniye tol keshid dg ta 3 montazer nabash


login = login(driver = driver)
main_page = mainPage(driver = driver)

login.enter_username('Admin')
login.enter_password('admin123')
login.click_on_login_button()
main_page.check_main_page()
sleep(2)