from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class SignInPage:
    def __init__(self):
        self.email_input = login_form.find_element_by_css_selector("input#login-email.login-email")
        self.pw_input = login_form.find_element_by_css_selector("input#login-password.login-password")


print("Webdriver Program Initiated... \n")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://linkedin.com")
job_title = "Software Engineer"
location = "United States"


assert "LinkedIn" in driver.title
try: 
    #Assert
    login_form = driver.find_element_by_class_name("login-form")
    
    sp = SignInPage()
   
    #email_input = login_form.find_element_by_css_selector("input#login-email.login-email")    
    sp.email_input.clear()
    sp.email_input.send_keys(email)
    
    #pw_input = login_form.find_element_by_css_selector("input#login-password.login-password")
    sp.pw_input.clear()
    sp.pw_input.send_keys(pw)    
    sp.email_input.send_keys(Keys.RETURN)

    #Assert
    jobs_button = driver.find_element_by_css_selector("li#jobs-nav-item.nav-item.nav-item--jobs")
    jobs_button.click()
    
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
   
