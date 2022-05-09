from pages.basePage import BasePage
from utils.locators import DetailPageLocators
from selenium.webdriver.support.ui import Select


class DetailPage(BasePage):
    def __init__(self, driver):
        self.locator = DetailPageLocators
        super().__init__(driver)

    def click_add_to_card_button(self):
        self.find_element(*self.locator.ADDTOCART).click()

    def click_buy_button(self):
        self.find_element(*self.locator.BUYNOW).click()

    def click_select_qty(self):
        return Select(self.find_element(*self.locator.SELECTQTY))

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_pass(self, pw):
        self.find_element(*self.locator.PASS).send_keys(pw)

    def enter_phone(self, ms):
        self.find_element(*self.locator.PHONE).send_keys(ms)

    def enter_address1(self, ms):
        self.find_element(*self.locator.ADDRESS1).send_keys(ms)

    def enter_address2(self, ms):
        self.find_element(*self.locator.ADDRESS2).send_keys(ms)

    def enter_city(self, ms):
        self.find_element(*self.locator.CITY).send_keys(ms)

    def enter_zipcode(self, ms):
        self.find_element(*self.locator.ZIPCODE).send_keys(ms)

    def click_continue_button(self):
        self.find_element(*self.locator.CONTINUE).click()

    def click_singin_button(self):
        self.find_element(*self.locator.SIGNIN).click()

    def click_default_address_checkbox(self):
        self.find_element(*self.locator.CHECKBOXDEFAULT).click()

    def click_submit_address_button(self):
        self.find_element(*self.locator.SUBMITADDRESS).click()

    def msg_check_value(self):
        msg = self.find_element(*self.locator.MSGVALUE).text
        return msg
