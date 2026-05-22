import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.lenovo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
