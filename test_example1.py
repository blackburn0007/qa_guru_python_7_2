import pytest
import json
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestExample1:
    @pytest.mark.usefixtures("driver")
    def test_search(self, driver):
        search_bar = driver.find_element(By.CSS_SELECTOR, "textarea[id='APjFqb']")
        search_bar.send_keys("QA Engineer jobs")
        search_bar.send_keys(Keys.ENTER)

    @pytest.mark.usefixtures("driver")
    def test_no_results(self, driver):
        search_phrase = "fsdfsdfsdfsdfsdfsdfgfsdgdfg"  # случайный набор символов
        search_bar = driver.find_element(By.CSS_SELECTOR, "textarea[id='APjFqb']")
        search_bar.send_keys(search_phrase)
        search_bar.send_keys(Keys.ENTER)
        results = driver.find_element(By.CSS_SELECTOR, "p[aria-level='3']")
        assert results.text == f'Ҷустуҷӯятон - "{search_phrase}" - дар ягон саҳифа ёфт нашуд.', "Результаты найдены"
