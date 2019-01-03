import traceback
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class PageObject(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
    
    def find_element(self, *loc):        
        return self.driver.find_element(*loc)
    
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def __getattr__(self, what):        
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_all_elements_located(
                        self.locator_dictionary[what])
                )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                try:
                    element = WebDriverWait(self.driver, self.timeout).until(
                    EC.visibility_of_all_elements_located(
                        self.locator_dictionary[what])
                )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
            
            if "multi" in what:                
                return self.find_elements(*self.locator_dictionary[what])
            else:
                print("Reached")
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locator_dictionary[what])            

            
        except AttributeError:
            raise AttributeError
            #super(PageObject, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print("No %s here!" % what) 
    
    def _wait_for_clickable_loc(self, loc):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(loc))
        except TimeoutException:
            traceback.print_exc()
    '''
    def _wait_for_clickable_ele(self, ele):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable())
        except TimeoutException:
            traceback.print_exc()
    '''


    def wait_click_loc(self, loc):
        self._wait_for_clickable_loc(loc)
        self.find_element(*loc).click()
    
    def wait_click_ele(self, ele):
        self._wait_for_clickable_loc(ele)
        ele.click()        
    
    def _wait_for_correct_text_input(self, loc, text):
        try:
            WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element_value(loc, text))
        except TimeoutException:
            self.wait_text_input(loc, text)          
            print(traceback.print_exc())               

    def wait_text_input(self, loc, text):        
        elem = self.find_element(*loc)
        elem.clear()
        elem.send_keys(text)        
        self._wait_for_correct_text_input(loc, text)