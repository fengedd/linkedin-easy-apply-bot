from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JobsListingPage(PageObject):
    
    def __init__(self, driver):
        super().__init__(driver)            
    
    locator_dictionary = {
        "filter_button": (By.CSS_SELECTOR, "button[data-control-name=\"all_filters\"]"),        
    }   

    def click_filter_button(self):
        loc = self.locator_dictionary["filter_button"]
        self.wait_click(loc)        
