from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import get_element, wait_visible
from src.PageObject.locators import Locators


class CheckboxPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_header(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            Locators.c_header_elements))
        )

    def home(self):
        return get_element(self.driver, Locators.c_checkbox_home)

    def wait_label_desktop(self):
        return wait_visible(self.driver, Locators.c_label_desktop)

    def wait_label_documents(self):
        return wait_visible(self.driver, Locators.c_label_documents)

    def wait_label_downloads(self):
        return wait_visible(self.driver, Locators.c_label_downloads)

    def wait_label_word_file(self):
        return wait_visible(self.driver, Locators.c_label_word_file)

    def wait_label_excel_file(self):
        return wait_visible(self.driver, Locators.c_label_word_file)

    def download(self):
        return get_element(self.driver, Locators.c_checkbox_downloads)

    def word_file(self):
        return get_element(self.driver, Locators.c_checkbox_word_file)

    def word_hint(self):
        if (wait_visible(self.driver, Locators.c_label_word_start_hint)
                is not None):
            return wait_visible(self.driver, Locators.c_label_word_finish_hint)
