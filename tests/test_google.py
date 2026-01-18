# def test_login():
#     print("Login test executed successfully")
#     assert True

# PyTest FIXTURES EXAMPLE:

# from pages.google_page import GooglePage
# from selenium.webdriver.common.by import By

# def test_google_search(setup):
#     driver = setup
#     google = GooglePage(driver)

#     google.search_text("Selenium WebDriver")
#     driver.find_element_by_name("q").send_keys(Keys.ENTER)

#     assert "Selenium" in driver.title
    
# 3 . test_loin.py:
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google_title():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)  # Wait for the page to load
    assert "Google" in driver.title
    driver.quit()
                
    