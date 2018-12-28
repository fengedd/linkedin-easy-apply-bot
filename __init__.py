from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.SignInPage import SignInPage
from PageObjects.HomePage import HomePage
from PageObjects.JobsListingPage import JobsListingPage
from PageObjects.JobsPage import JobsPage

print("Webdriver Program Initiated... \n")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://linkedin.com")
job_title = "Software Engineer"
location = "United States"



assert "LinkedIn" in driver.title
try:
    # Assert
    sign_in_page = SignInPage(driver)
    sign_in_page.enter_email(email)
    sign_in_page.enter_password(pw)
    sign_in_page.submit()
    # Assert
    home_page = HomePage(driver)
    home_page.click_jobs_button()
    # Assert
    jobs_page = JobsPage(driver)
    jobs_page.enter_job(job_title)
    jobs_page.enter_location(location)
    jobs_page.submit()

    # Assert
    jobs_listing_page = JobsListingPage(driver)
    driver.implicitly_wait(10)
    jobs_listing_page.click_filter_button()
    driver.implicitly_wait(10)
    jobs_listing_page.click_easy_apply()
    jobs_listing_page.click_intership()
    jobs_listing_page.click_entry_level()
    jobs_listing_page.click_associate()
    driver.implicitly_wait(10)
    jobs_listing_page.click_apply_filter_button()

    job_display_panes = driver.find_element_by_css_selector(
        "div.jobs-search-two-pane__wrapper.jobs-search-two-pane__wrapper--two-pane")
    search_results_pane = job_display_panes.find_element(
        "div.jobs-search-results.jobs-search-results--is-two-pane")


except NoSuchElementException:
    print('Exception!')
