import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    # Initialize Chrome driver
    with webdriver.Chrome(service=Service()) as driver:
        driver.maximize_window()
        driver.get("https://google.com")
        yield driver


def logger(level):
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("logger.log")
    formatter = logging.Formatter("%(asctime)s :% (levelname)s : % (name)s : %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(level)
