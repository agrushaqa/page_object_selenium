import pytest

from src.PageObject.checkbox_page import CheckboxPage
from src.PageObject.elements_page import ElementsPage
from src.PageObject.main_page import MainPage


class TestOpenPages:

    @pytest.mark.parametrize("page_url",
                             [("https://demoqa.com/")])
    def test_open_elements(self, web_driver, page_url):
        web_driver.get(page_url)
        main_page = MainPage(web_driver)
        main_page.wait_and_click_on_elements()
        elements_page = ElementsPage(web_driver)
        assert elements_page.wait_header() is not None
        assert web_driver.current_url == "https://demoqa.com/elements"

    @pytest.mark.parametrize("page_url",
                             [("https://demoqa.com/")])
    def test_open_checkbox(self, web_driver, page_url):
        web_driver.get(page_url)
        main_page = MainPage(web_driver)
        main_page.wait_and_click_on_elements()
        elements_page = ElementsPage(web_driver)
        elements_page.wait_header()
        elements_page.checkbox().click()
        checkbox_page = CheckboxPage(web_driver)
        checkbox_page.wait_header()
        assert web_driver.current_url == "https://demoqa.com/checkbox"

