from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import get_element
from src.PageObject.locators import Locators


class ElementsPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_header(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                Locators.e_header_elements))
            )
        except Exception as e:
            logger.debug(e)
            return None

    def checkbox(self):
        return get_element(self.driver, Locators.e_checkbox)
