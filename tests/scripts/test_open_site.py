import pytest


class TestOpenSite:

    @pytest.mark.parametrize("page_url, expected_title",
                             [("https://demoqa.com/", "DEMOQA")])
    def test_open_site(self, web_driver, page_url, expected_title):
        web_driver.get(page_url)
        assert web_driver.title == expected_title
