from locators import *


class login:
  def __init__(self,driver):
    self.driver = driver
    

  def enter_username(self, username):
    self.driver.find_element('name', username_textbox_name).send_keys(username)

  def enter_password(self, password):
    self.driver.find_element('name', username_textbox_name).send_keys(password)

  def click_on_login_button(self):
    self.driver.find_element('class', login_button_class)


# <input data-v-1f99f73c="" class="oxd-input oxd-input--active" name="username" placeholder="Username" autofocus="">
# <input data-v-1f99f73c="" class="oxd-input oxd-input--active" type="password" name="password" placeholder="Password">