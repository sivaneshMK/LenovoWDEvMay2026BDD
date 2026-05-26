import allure
import pytest
from selenium import webdriver

from pages.home_page import HomePage


@pytest.fixture(scope="function")
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
        #driver = getattr(item, "driver")
        print("The driver is not closed")
        try:
            if driver:
                path = "C:\\Users\\sivan\\PycharmProjects\\Lenovo_BDD_MayWD2026\\screenshots\\screenshot.png"
                driver.save_screenshot(path)
                allure.attach(
                    path,
                    name="Failure_Screenshot",
                    attachment_type= allure.attachment_type.PNG

                )
                print("attached the screenshots in to the report")
        except Exception as e:
            print(f"Couldn't able to attach the screenshots {e}")
