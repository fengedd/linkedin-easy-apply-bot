
from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys

class SignInPage(PageObject):
    def __init__(self, driver):
        # login_form = driver.find_element_by_class_name("login-form")
        super().__init__(driver)
        self.email_input = driver.find_element_by_css_selector(
            "input#login-email.login-email")
        self.pw_input = driver.find_element_by_css_selector(
            "input#login-password.login-password")

    def enter_email(self, email):
        self.email_input.clear()
        self.email_input.send_keys(email)

    def enter_password(self, password):
        self.pw_input.clear()
        self.pw_input.send_keys(password)

    def submit(self):
        self.pw_input.send_keys(Keys.RETURN)