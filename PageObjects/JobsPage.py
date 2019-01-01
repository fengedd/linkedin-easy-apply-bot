from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class JobsPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)        
    
    locator_dictionary = {
        "jobs_search_box_input": (By.CSS_SELECTOR, "div.jobs-search-box__input.jobs-search-box__input--keyword input:nth-child(2)"),
        "location_search_box_input": (By.CSS_SELECTOR, "div.jobs-search-box__input.jobs-search-box__input--location input:nth-child(2)"),
        "search_button": (By.CSS_SELECTOR, "button.jobs-search-box__submit-button")
    }   

    def click_search_button(self):                
        loc = self.locator_dictionary["search_button"]
        self.wait_click(loc)
        WebDriverWait(self.driver, 5).until(EC.url_changes)        

    def enter_job(self, job_title):
        loc = self.locator_dictionary["jobs_search_box_input"]
        self.wait_text_input(loc, job_title)        

    def enter_location(self, location):
        loc = self.locator_dictionary["location_search_box_input"]
        self.wait_text_input(loc, location)