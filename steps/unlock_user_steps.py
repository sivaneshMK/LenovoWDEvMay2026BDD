import time

from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# this line will help to connet feature file and step definition file

scenarios("../features/unlock_account.feature")

@given("launch the application")
def func(driver):
    print("application is launched successfully")

@when("user enter name, email, and country")
def fun(driver):
    driver.implicitly_wait(20)
    driver.find_element(By.NAME,"first_name").send_keys("abcdefgh")
    driver.find_element(By.NAME, "email").send_keys("abcd@gmail.com")

    element = driver.find_element(By.XPATH, "//select[@name='country']")
    s1 = Select(element)
    s1.select_by_value("CN")

@when("select terms and conditions check box")
def fun(driver):
    driver.find_element(By.XPATH, "//input[@name='email_permission_status']/..").click()
    driver.find_element(By.XPATH, "//input[@name='enhanced_experience_status']/..").click()

@when("click on unlocak offer")
def fun(driver):
    driver.find_element(By.XPATH, "//button[@name='bluecoreEmailCaptureSubmit']").click()

@then("validate  full name, email id. section")
def fun(driver):
    print("Test pass")
    time.sleep(10)