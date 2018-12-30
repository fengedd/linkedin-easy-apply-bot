
from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SignInPage(PageObject):
    def __init__(self, driver):        
        super().__init__(driver)        
    
    locator_dictionary = {
        "email_input": (By.CSS_SELECTOR, "input#login-email.login-email"),        
        "pw_input": (By.CSS_SELECTOR, "input#login-password.login-password"),
        "sign_in_button": (By.CSS_SELECTOR, "#login-submit")        
    }   

    def click_sign_in_button(self):
        self.find_element(*self.locator_dictionary["sign_in_button"]).click()

    def enter_email(self, email):
        elem = self.find_element(*self.locator_dictionary["email_input"])
        elem.clear()
        elem.send_keys(email)     

    def enter_password(self, password):
        elem = self.find_element(*self.locator_dictionary["pw_input"])
        elem.clear()
        elem.send_keys(password)   