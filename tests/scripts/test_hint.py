import pytest

from src.PageObject.checkbox_page import CheckboxPage


class TestHint:

    @pytest.mark.parametrize("page_url",
                             [("https://demoqa.com/checkbox")])
    def test_hint_for_word_file(self, web_driver, page_url):
        web_driver.get(page_url)
        checkbox_page = CheckboxPage(web_driver)
        checkbox_page.wait_header()
        checkbox_page.home().click()
        checkbox_page.wait_label_downloads()
        checkbox_page.download().click()
        checkbox_page.wait_label_word_file()
        checkbox_page.word_file().click()
        assert checkbox_page.word_hint() is not None
