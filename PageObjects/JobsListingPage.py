from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions    import NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

class JobListing(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
    
    locator_dictionary = {
        "easy_one_click_apply_button": (By.CSS_SELECTOR, "button.jobs-apply-button"),
        "applied_check_mark_icon_pred": (By.CSS_SELECTOR, "li-icon.artdeco-inline-feedback__icon"),
        "easy_apply_submit_button": (By.CSS_SELECTOR, "div.jobs-apply-form__footer-buttons.display-flex > button.jobs-apply-form__submit-button.button-primary-large"),
        "one_click_apply_close_window_button": (By.CSS_SELECTOR, "button.artdeco-dismiss"),
        "job_title": (By.CSS_SELECTOR, "h1.jobs-details-top-card__job-title")        
    }
    '''
    def get_job_title(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html)
        title = soup.find_element("h1.jobs-details-top-card__job-title").getText()        
        return title
    '''  

    def has_applied(self):
        loc = self.locator_dictionary["applied_check_mark_icon_pred"]
        try:
            self.find_element(*loc)
            return True
        except NoSuchElementException:
            return False
    
    def is_one_click_apply_closeable(self):
        loc = self.locator_dictionary["one_click_apply_close_window_button"]
        try:
            self.find_element(*loc)
            return True
        except NoSuchElementException:
            return False
    
    def click_easy_one_click_apply_button(self):
        loc = self.locator_dictionary["easy_one_click_apply_button"]
        self.wait_click_loc(loc)

    def close_one_click_apply_window(self):
        loc = self.locator_dictionary["one_click_apply_close_window_button"]
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
        except Exception:
            raise Exception
        self.wait_click_loc(loc)


class JobsListingPage(PageObject):
    
    def __init__(self, driver):
        super().__init__(driver)
        #jobs_pane = "ul.jobs-search-results__list"  
        #pagination_buttons = "section.search-results-pagination-section ol>li>ol>li" 
        # New window is opened
        # easy_apply_phone_num = "input[autocomplete=\"tel-national\"]"
        # work_authorization_inputs = "div.work-authorization-group input" ##buttons 2 and 3
        # easy_apply_submit_button = "button.continue-btn"
        # close window

    
    locator_dictionary = {
        "filter_button": (By.CSS_SELECTOR, "button[data-control-name=\"all_filters\"]"),        
        "listings_multi": (By.CSS_SELECTOR, "div h3 a.job-card-search__link-wrapper"),
        "one_click_apply_close_window_button": (By.CSS_SELECTOR, "button.artdeco-dismiss"),                
        "next_page_button": (By.CSS_SELECTOR, "section.search-results-pagination-section ol>li>ol>li.active + li"),       

    }   

    def click_filter_button(self):
        loc = self.locator_dictionary["filter_button"]
        self.wait_click_loc(loc)
    
    def get_listings(self):
        loc = self.locator_dictionary["listings_multi"]                      
        return self.find_elements(*loc)
    
    def click_given_listing(self, num):
        ele = self.get_listings()[num]
        ele.click()        
    
    def go_next_page(self):
        loc = self.locator_dictionary["next_page_button"]
        self.wait_click_loc(loc)
    
    def easy_apply_active(self):
        return len(self.driver.window_handles) > 1
    
    def wait_for_easy_apply_to_complete(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.number_of_windows_to_be(1))
        except Exception:
            raise Exception                     

