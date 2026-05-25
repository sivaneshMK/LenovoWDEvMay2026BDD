from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    USERNAME_TXT_BX = (By.NAME,"first_name")
    EMAIL_TXT_BX = (By.NAME, "email")
    COUNTRY_LIST_BX = (By.XPATH, "//select[@name='country']")
    UNLOCK_POPUP = (By.XPATH, "//div[@id='bluecoreActionScreen']")
    EMAIL_PERMISION_CHECK_BOX = (By.XPATH, "//input[@name='email_permission_status']/..")
    TERMS_AND_CONDITION_CHECK_BOX = (By.XPATH, "//input[@name='enhanced_experience_status']/..")
    UNLOCK_OFFER_BTN = (By.XPATH, "//button[@name='bluecoreEmailCaptureSubmit']")
    UNLOCK_POPUP_CLOSE_BTN =(By.XPATH, "(//button[@name='bluecoreCloseButton'])[1]")
    PRODUCT_SEARCH_BOX = (By.XPATH, "//input[@name='commonHeaderSearch']")
    DECLINE_OFFER_LINK = (By.XPATH, "//button[text()='Decline Offer']")
    

    def enter_username(self, username):
        self.enter_text(self.USERNAME_TXT_BX, username, "User name Text Box")

    def enter_email_id(self, emailid):
        self.enter_text(self.EMAIL_TXT_BX, emailid, "Email Id Text Box")

    def select_country(self, country):
        self.select_by_value(self.COUNTRY_LIST_BX, country, "Country List Box")

    def wait_until_unlock_popup_displayed(self):

        self.is_displayed(self.UNLOCK_POPUP, "Unlock Popup")

    def click_on_term_and_conditions_check_box(self):
        self.select_check_box(self.TERMS_AND_CONDITION_CHECK_BOX, "Term and Condition Check box")

    def click_on_email_permission_check_box(self):
        self.select_check_box(self.EMAIL_PERMISION_CHECK_BOX, "Email Permission Check Box")

    def click_on_unlock_offer_button(self):
        self.click(self.UNLOCK_OFFER_BTN, "Unlock offer button")

    def close_unlock_popup(self):
        self.click(self.UNLOCK_POPUP_CLOSE_BTN, "Unlock popup close button")

    def enter_search_string(self, product_name):
        self.enter_text(self.PRODUCT_SEARCH_BOX, product_name, "Product search box")

    def decline_offer(self):
        self.click(self.DECLINE_OFFER_LINK, "decline offer link")