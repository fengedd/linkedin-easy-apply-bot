from .PageObject import PageObject
from selenium.webdriver.common.keys import Keys
class JobsPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.jobs_search_box_input = driver.find_element_by_css_selector(
            "div.jobs-search-box__input.jobs-search-box__input--keyword").find_elements_by_tag_name("input")[1]
        self.location_search_box_input = driver.find_element_by_css_selector(
            "div.jobs-search-box__input.jobs-search-box__input--location").find_elements_by_tag_name("input")[1]

    def enter_job(self, job_title):
        self.jobs_search_box_input.clear()
        self.jobs_search_box_input.send_keys(job_title)

    def enter_location(self, location):
        self.location_search_box_input.clear()
        self.location_search_box_input.send_keys(location)

    def submit(self):
        self.location_search_box_input.send_keys(Keys.RETURN)