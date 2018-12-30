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
