from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Locators import JobsListingPageLocators


class JobsListingPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(driver, 3)
        self.filter_button = driver.find_element(*JobsListingPageLocators.FILTER_BUTTON)

        #self.filter_button = wait.until(
        #    EC.presence_of_element_located(JobsListingPageLocators.FILTER_BUTTON))

    def click_filter_button(self):
        self.filter_button.click()
        #self.driver.find_element(*JobsListingPageLocators.FILTER_BUTTON)
