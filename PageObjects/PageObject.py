import traceback
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageObject(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
    
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def __getattr__(self, what):        
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located(
                        self.locator_dictionary[what])
                )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.driver, self.timeout).until(
                    EC.visibility_of_element_located(
                        self.locator_dictionary[what])
                )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
            # I could have returned element, however because of lazy loading, I am seeking the element before return
            return self.find_element(*self.locator_dictionary[what])            
        except AttributeError:
            raise AttributeError
            #super(PageObject, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print("No %s here!" % what) 
    
    def _wait_for_clickable(self, loc):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(loc))
    
    def wait_click(self, loc):
        self._wait_for_clickable(loc)
        self.find_element(*loc).click()
    
    def _wait_for_text(self, loc, text):
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element_value(loc, text))

    def wait_text_input(self, loc, text):
        elem = self.find_element(*loc)
        elem.clear()        
        elem.send_keys(text)
        self._wait_for_text(loc, text)

        
