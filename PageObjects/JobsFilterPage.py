from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class JobsFilterPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(driver, 3)                    
        form = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "ul.search-advanced-facets__facets-list")))
        # form = driver.find_element_by_css_selector("ul.search-advanced-facets__facets-list")
        self.linkedin_features_form_inputs = form.find_element_by_css_selector(
            "div#linkedin-features-facet-values").find_elements_by_css_selector("li")
        self.date_posted_form = form.find_element_by_css_selector(
            "#date-posted-facet-values")
        self.job_type_form = form.find_element_by_css_selector(
            "#job-type-facet-values")
        self.experience_level_form_inputs = form.find_element_by_css_selector(
            "#experience-level-facet-values").find_elements_by_css_selector("li")
        self.easy_apply_label = self.linkedin_features_form_inputs[0]
        self.in_network_label = self.linkedin_features_form_inputs[1]
        self.under_10_applicants_label = self.linkedin_features_form_inputs[2]
        self.internship_label = self.experience_level_form_inputs[0]
        self.entry_level_label = self.experience_level_form_inputs[1]
        self.associate_label = self.experience_level_form_inputs[2]
        self.apply_filter_button = driver.find_element_by_css_selector(
            "button.search-advanced-facets__button--apply.button-primary-large")

    def click_easy_apply(self):
        self.easy_apply_label.click()

    def click_in_network(self):
        self.in_network_label.click()

    def click_under_10_applicants(self):
        self.under_10_applicants_label.click()

    def click_intership(self):
        self.internship_label.click()

    def click_entry_level(self):
        self.entry_level_label.click()

    def click_associate(self):
        self.associate_label.click()

    def click_apply_filter_button(self):
        self.apply_filter_button.click()