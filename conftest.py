import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    # Initialize Chrome driver
    with webdriver.Chrome(service=Service()) as driver:
        driver.maximize_window()
        driver.get("https://google.com")
        yield driver

