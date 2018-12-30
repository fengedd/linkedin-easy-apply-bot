from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.SignInPage import SignInPage
from PageObjects.HomePage import HomePage
from PageObjects.JobsListingPage import JobsListingPage
from PageObjects.JobsPage import JobsPage
from PageObjects.JobsFilterPage import JobsFilterPage
import time

print("Webdriver Program Initiated... \n")
website = "https://linkedin.com"
job_title = "Software Engineer"
location = "United States"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get(website)

assert "LinkedIn" in driver.title
try:
    # Assert
    sign_in_page = SignInPage(driver)
    sign_in_page.enter_email(email)
    sign_in_page.enter_password(pw)
    sign_in_page.click_sign_in_button()
    # Assert
    home_page = HomePage(driver)
    home_page.click_jobs_button()
    # Assert
    jobs_page = JobsPage(driver)
    jobs_page.enter_job(job_title)
    jobs_page.enter_location(location)
    jobs_page.click_search_button()

    # Assert    
    jobs_listing_page = JobsListingPage(driver)    
    jobs_listing_page.click_filter_button()
    
    jobs_filter_page = JobsFilterPage(driver)    
    time.sleep(4)
    jobs_filter_page.click_easy_apply()
    jobs_filter_page.click_exp_intership()
    jobs_filter_page.click_entry_level()
    jobs_filter_page.click_associate()
    time.sleep(4)
    jobs_filter_page.click_apply_filter_button()    
 
except NoSuchElementException:    
    print('Exception!')
