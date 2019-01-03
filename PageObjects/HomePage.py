from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HomePage(PageObject):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)        

    locator_dictionary = {
        "jobs_button": (By.CSS_SELECTOR, "li#jobs-nav-item.nav-item.nav-item--jobs"),        
    }    

    def click_jobs_button(self):
        loc = self.locator_dictionary["jobs_button"]
        self.wait_click_loc(loc)