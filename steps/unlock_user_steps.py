import time

import pytest
from gherkin import parser
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import pages.home_page

# this line will help to connet feature file and step definition file

scenarios("../features/unlock_account.feature")

# @pytest.fixture
# def get_driver(driver):
#     return driver

#home_page = HomePage(get_driver)
@given("launch the application")
def func(pages):
    print("application is launched successfully")

@when("user enter name, email, and country")
def fun(pages):
    # driver.implicitly_wait(20)
    # driver.find_element(By.NAME,"first_name").send_keys("abcdefgh")
    # driver.find_element(By.NAME, "email").send_keys("abcd@gmail.com")
    #
    # element = driver.find_element(By.XPATH, "//select[@name='country']")
    # s1 = Select(element)
    # s1.select_by_value("CN")
    # home_page = HomePage(driver)
    # home_page.
    pages.home_page.wait_until_unlock_popup_displayed()
    pages.home_page.enter_username("sivanesh")
    pages.home_page.enter_email_id("sivanesh@gmail.com")
    pages.home_page.select_country("CN")

@when("select terms and conditions check box")
def fun(pages):
    # driver.find_element(By.XPATH, "//input[@name='email_permission_status']/..").click()
    # driver.find_element(By.XPATH, "//input[@name='enhanced_experience_status']/..").click()
    pages.home_page.click_on_email_permission_check_box()
    pages.home_page.click_on_term_and_conditions_check_box()


@when("click on unlocak offer")
def fun(pages):
    # driver.find_element(By.XPATH, "//button[@name='bluecoreEmailCaptureSubmit']").click()
    pages.home_page.click_on_unlock_offer_button()

@then("validate  full name, email id. section")
def fun(driver):
    print("Test pass")
    assert "abcd"== "xyz", "The output is not valid"

@when(parsers.parse('enter "{product_name}" in search box'))
def fun(pages, product_name):
    pages.home_page.decline_offer()
    pages.home_page.enter_search_string(product_name)
    time.sleep(10)