from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
class HomePage(PageObject):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.jobs_button = driver.find_element_by_css_selector(
            "li#jobs-nav-item.nav-item.nav-item--jobs")

    def click_jobs_button(self):
        self.jobs_button.click()