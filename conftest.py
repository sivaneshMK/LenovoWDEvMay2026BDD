import allure
import pytest
from selenium import webdriver

from pages.home_page import HomePage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.lenovo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def pages(driver):
    class Pages:
        home_page = HomePage(driver)

    return Pages()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure_Screenshot",
                attachment_type= allure.attachment_type.PNG
            )
