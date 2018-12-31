from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

    def enter_job(self, job_title):
        elem = self.find_element(*self.locator_dictionary["jobs_search_box_input"])
        elem.clear()
        elem.send_keys(job_title)        

    def enter_location(self, location):
        elem = self.find_element(*self.locator_dictionary["location_search_box_input"])
        elem.clear()
        elem.send_keys(location)