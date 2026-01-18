import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    yield driver        # test runs here
    driver.quit()       # runs after test