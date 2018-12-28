from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class PageObject:
    def __init__(self, driver):
        self.__driver = driver

class SignInPage(PageObject):
    def __init__(self, driver):
        # login_form = driver.find_element_by_class_name("login-form")  
        super().__init__(self, driver)
        self.email_input = driver.find_element_by_css_selector("input#login-email.login-email")
        self.pw_input = driver.find_element_by_css_selector("input#login-password.login-password")
        
    
    def enter_email(self, email):
        self.email_input.clear()
        self.email_input.send_keys(email)

    def enter_password(self, password):
        self.pw_input.clear()
        self.pw_input.send_keys(password)

    def submit(self):
        self.pw_input.send_keys(Keys.RETURN)

class HomePage(PageObject):
    def __init__(self, driver):
        super().__init__(self, driver)
        self.jobs_button = driver.find_element_by_css_selector("li#jobs-nav-item.nav-item.nav-item--jobs")
    
    def click_jobs_button(self):
        self.jobs_button.click()       
        
    


print("Webdriver Program Initiated... \n")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://linkedin.com")
job_title = "Software Engineer"
location = "United States"

assert "LinkedIn" in driver.title
try: 
    #Assert      
    sign_in_page = SignInPage(driver)      
    sign_in_page.enter_email(email)
    sign_in_page.enter_password(pw)
    sign_in_page.submit()
    #Assert
    home_page = HomePage(driver)
    home_page.click_jobs_button()    
    #Assert
    jobs_search_box = driver.find_element_by_css_selector("div.jobs-search-box__input.jobs-search-box__input--keyword")
    jobs_search_box_input = jobs_search_box.find_elements_by_tag_name("input")[1]
    jobs_search_box_input.clear()
    jobs_search_box_input.send_keys(job_title)

    location_search_box = driver.find_element_by_css_selector("div.jobs-search-box__input.jobs-search-box__input--location")
    location_search_box_input = location_search_box.find_elements_by_tag_name("input")[1]
    location_search_box_input.clear()
    location_search_box_input.send_keys(location)
    location_search_box_input.send_keys(Keys.RETURN)
    

    #Assert    
    driver.implicitly_wait(10)
    filter_button = driver.find_element_by_css_selector("button[data-control-name=\"all_filters\"]")
    filter_button.click()
    driver.implicitly_wait(10)
    filter_form = driver.find_element_by_css_selector("ul.search-advanced-facets__facets-list")
    linkedin_features_form_inputs = filter_form.find_element_by_css_selector("div#linkedin-features-facet-values").find_elements_by_css_selector("li")
    date_posted_form = filter_form.find_element_by_css_selector("#date-posted-facet-values")
    job_type_form = filter_form.find_element_by_css_selector("#job-type-facet-values")     
    experience_level_form_inputs = filter_form.find_element_by_css_selector("#experience-level-facet-values").find_elements_by_css_selector("li")
    driver.implicitly_wait(10)
    easy_apply_label = linkedin_features_form_inputs[0] 
    in_network_label = linkedin_features_form_inputs[1]
    under_10_applicants_label = linkedin_features_form_inputs[2]
    driver.implicitly_wait(10)
    easy_apply_label.click()
    driver.implicitly_wait(10)
    internship_label = experience_level_form_inputs[0] 
    entry_level_label = experience_level_form_inputs[1] 
    associate_label = experience_level_form_inputs[2] 
    driver.implicitly_wait(10)
    internship_label.click()
    entry_level_label.click()
    associate_label.click()

    apply_filter_button = driver.find_element_by_css_selector("button.search-advanced-facets__button--apply.button-primary-large")
    apply_filter_button.click()



    job_display_panes = driver.find_element_by_css_selector("div.jobs-search-two-pane__wrapper.jobs-search-two-pane__wrapper--two-pane")
    search_results_pane = job_display_panes.find_element("div.jobs-search-results.jobs-search-results--is-two-pane")







    
    
    
    
except NoSuchElementException:
    print('Exception!')
   
