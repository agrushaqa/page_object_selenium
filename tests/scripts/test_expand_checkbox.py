import pytest

from src.PageObject.checkbox_page import CheckboxPage


class TestExpandCheckbox:

    @pytest.mark.parametrize("page_url",
                             [("https://demoqa.com/checkbox")])
    def test_checkbox_home(self, web_driver, page_url):
        web_driver.get(page_url)
        checkbox_page = CheckboxPage(web_driver)
        checkbox_page.wait_header()
        checkbox_page.home().click()
        assert checkbox_page.wait_label_desktop() is not None
        assert checkbox_page.wait_label_documents() is not None
        assert checkbox_page.wait_label_downloads() is not None

    @pytest.mark.parametrize("page_url",
                             [("https://demoqa.com/checkbox")])
    def test_checkbox_download(self, web_driver, page_url):
        web_driver.get(page_url)
        checkbox_page = CheckboxPage(web_driver)
        checkbox_page.wait_header()
        checkbox_page.home().click()
        checkbox_page.wait_label_downloads()
        checkbox_page.download().click()
        assert checkbox_page.wait_label_word_file() is not None
        assert checkbox_page.wait_label_excel_file() is not None
