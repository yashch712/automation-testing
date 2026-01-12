# def test_login():
#     print("Login test executed successfully")
#     assert True

# PyTest FIXTURES EXAMPLE:
import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    yield driver        # test runs here
    driver.quit()       # runs after test


def test_google_title(setup):
    driver = setup
    assert "Google" in driver.title

def test_url(setup):
    assert "google.com" in setup.current_url