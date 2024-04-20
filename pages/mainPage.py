from locators import *


class mainPage:
    def __init__(self, driver):
        self.driver = driver

    def check_main_page(self):
        self.driver.find_element('class', dashboard_img_class)



# <span data-v-7b563373="" data-v-6475d26d="" class="oxd-text oxd-text--span oxd-main-menu-item--name">Dashboard</span>
# <span data-v-7b563373="" data-v-6475d26d="" class="oxd-text oxd-text--span oxd-main-menu-item--name">Performance</span>