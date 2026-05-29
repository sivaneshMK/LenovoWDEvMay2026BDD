import time

import allure
import pytest
from gherkin import parser
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import pages.home_page
from utility.read_test_data import ExcelReader

# this line will help to connet feature file and step definition file

scenarios("../features/unlock_account.feature")

# @pytest.fixture
# def get_driver(driver):
#     return driver

test_data = ExcelReader()
#home_page = HomePage(get_driver)
allure.tag("Regression")

@given("launch the application")
def func(request, pages):
    print("application is launched successfully")
    # to get the scenario name
    print(request.node.name)
    #print(pytestbdd_stepdef_given)
    #print(pytestdbb_stepfunc_args)
    #print(pytest_bdd_step_name)

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
    pages.home_page.enter_username(test_data.get_test_data("username"))# get_test_data("username")
    pages.home_page.enter_email_id(test_data.get_test_data("email"))
    pages.home_page.select_country(test_data.get_test_data("country"))


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
    #pages.home_page.enter_search_string(product_name)
    pages.home_page.enter_search_string(test_data.get_test_data("product_name"))
    time.sleep(10)

@given(parsers.parse("user credentials"))
def fun(datatable):
    print(datatable)

@when(parsers.parse('enter "{username}" "{password}"'))
def fun(username, password):
    print(username, password)
