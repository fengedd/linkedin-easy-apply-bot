from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class JobsFilterPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)      
    
    locator_dictionary = {
        "apply_filter_button": (By.CSS_SELECTOR, "button.search-advanced-facets__button--apply.button-primary-large"), 
        "easy_apply_box": (By.CSS_SELECTOR, "div#linkedin-features-facet-values li:nth-child(1)"),
        "in_network_box": (By.CSS_SELECTOR, "div#linkedin-features-facet-values li:nth-child(2)"),
        "under_10_applicants_box": (By.CSS_SELECTOR, "div#linkedin-features-facet-values li:nth-child(3)"),
        
        "exp_internship_box": (By.CSS_SELECTOR, "#experience-level-facet-values li:nth-child(1)"),
        "entry_level_box": (By.CSS_SELECTOR, "#experience-level-facet-values li:nth-child(2)"),
        "associate_box": (By.CSS_SELECTOR, "#experience-level-facet-values li:nth-child(3)"),
        "mid_senior_box": (By.CSS_SELECTOR, "#experience-level-facet-values li:nth-child(4)"),
        "director_box": (By.CSS_SELECTOR, "#experience-level-facet-values li:nth-child(5)"),
        "executive_box": (By.CSS_SELECTOR, "#experience-level-facet-values li:nth-child(6)"),

        "full_time_box": (By.CSS_SELECTOR, "#job-type-facet-values li:nth-child(1)"),
        "contract_box": (By.CSS_SELECTOR, "#job-type-facet-values li:nth-child(2)"),
        "job_internship_box": (By.CSS_SELECTOR, "#job-type-facet-values li:nth-child(3)"),
        "part_time_box": (By.CSS_SELECTOR, "#job-type-facet-values li:nth-child(4)"),
        "temporary_box": (By.CSS_SELECTOR, "#job-type-facet-values li:nth-child(5)"),
        "volunteer_box": (By.CSS_SELECTOR, "#job-type-facet-values li:nth-child(6)"),
        "other_box": (By.CSS_SELECTOR, "#job-type-facet-values li:nth-child(7)"),
    }   

    def click_apply_filter_button(self):
        self.find_element(*self.locator_dictionary["apply_filter_button"]).click()

    def click_easy_apply(self):
        self.find_element(*self.locator_dictionary["easy_apply_box"]).click()

    def click_in_network(self):
        self.find_element(*self.locator_dictionary["in_network_box"]).click()

    def click_under_10_applicants(self):
        self.find_element(*self.locator_dictionary["under_10_applicants_box"]).click()

    def click_exp_intership(self):
        self.find_element(*self.locator_dictionary["exp_internship_box"]).click()

    def click_entry_level(self):
        self.find_element(*self.locator_dictionary["entry_level_box"]).click()

    def click_associate(self):
        self.find_element(*self.locator_dictionary["associate_box"]).click()
