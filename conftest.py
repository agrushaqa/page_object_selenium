import time

import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="session")
def web_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver


def page_is_loading(driver):
    while True:
        x = driver.execute_script("return document.readyState")
        if x == "complete":
            return True
        else:
            yield False


def wait_and_click(driver, locator, timout=30):
    page_position = 10
    for _ in range(timout):
        try:
            element = driver.find_element(By.XPATH, locator)
            ActionChains(driver).scroll_by_amount(0, page_position).perform()
            time.sleep(1)
            ActionChains(driver).move_to_element(element).perform()
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, locator)))
            element.click()
            return
        except Exception:
            page_position += 20


def get_element(driver, locator):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, locator))
    )
    return driver.find_element(By.XPATH, locator)


def wait_visible(driver, localor):
    try:
        return WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, localor))
        )
    except Exception as e:
        logger.debug(e)
        return None
