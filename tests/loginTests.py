from pages.login import login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pages.mainPage import mainPage
import unittest


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3) # yani ta 3 saniye vasta ta amaliyat anjam beshe age 1 saniye tol keshid dg ta 3 montazer nabash
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        login = login(driver = self.driver)
        main_page = mainPage(driver = self.driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_on_login_button()
        main_page.check_main_page()
        sleep(2)

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.close()
        self.driver.quit()