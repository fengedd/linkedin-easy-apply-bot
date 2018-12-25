from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

print("Webdriver Program Initiated... \n")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://linkedin.com")
job_title = "Software Engineer"
location = "United States"

wait= WebDriverWait(driver,1)
assert "LinkedIn" in driver.title
try: 
    #Assert
    login_form = driver.find_element_by_class_name("login-form")
    
    email_input = login_form.find_element_by_css_selector("input#login-email.login-email")    
    email_input.clear()
    email_input.send_keys(email)
    
    
    pw_input = login_form.find_element_by_css_selector("input#login-password.login-password")
    pw_input.clear()
    pw_input.send_keys(pw)
    
    email_input.send_keys(Keys.RETURN)

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

    filter_form = driver.find_element_by_css_selector("ul.search-advanced-facets__facets-list")
    linkedin_features_form = filter_form.find_element_by_css_selector("div#linkedin-features-facet-values")
    date_posted_form = filter_form.find_element_by_css_selector("#date-posted-facet-values")
    job_type_form = filter_form.find_element_by_css_selector("#job-type-facet-values")     
    experience_level_form = filter_form.find_element("#experience-level-facet-values")



    
    
    
    
except NoSuchElementException:
    print('Exception!')
   
