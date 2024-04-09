class login:
  def __init__(self,driver):
    self.driver = driver
    self.username_textbox_name = 'username'
    self.username_texbox_password = 'password'
    self.login_button_class = 'orangehrm-login-button'

    def enter_username(self, username):
      self.driver.find_element('name',self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
      self.driver.find_element('name',self.username_textbox_password).send_keys(password)

    def click_on_login_button(self):
      self.driver.find_element('class', self.login_button_class)