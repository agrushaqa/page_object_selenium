from selenium.webdriver.remote import webelement

from conftest import wait_and_click
from src.PageObject.locators import Locators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_click_on_elements(self) -> webelement:
        return wait_and_click(self.driver, Locators.m_label_elements)
