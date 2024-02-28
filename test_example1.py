from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from BaseClass import BaseClass


class TestExample1(BaseClass):
    def test_search(self, driver):
        search_bar = driver.find_element(By.CSS_SELECTOR, "textarea[id='APjFqb']")
        search_bar.send_keys("QA Engineer jobs")
        search_bar.send_keys(Keys.ENTER)
        log = self.get_logger()
        log.info("Searching is operational")

    def test_no_results(self, driver):
        search_phrase = "fsdfsdfsdfsdfsdfsdfgfsdgdfg"  # случайный набор символов
        search_bar = driver.find_element(By.CSS_SELECTOR, "textarea[id='APjFqb']")
        search_bar.send_keys(search_phrase)
        search_bar.send_keys(Keys.ENTER)
        results = driver.find_element(By.CSS_SELECTOR, "p[aria-level='3']")
        assert results.text == f'Ҷустуҷӯятон - "{search_phrase}" - дар ягон саҳифа ёфт нашуд.', "Результаты найдены"
        log = self.get_logger()
        log.info("No search results were displayed")