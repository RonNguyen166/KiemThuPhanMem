from pages.homePage import *
from utils.locators import *
from pages.basePage import BasePage
from utils import users


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_continue_button(self):
        self.find_element(*self.locator.CONTINUE).click()

    def click_continue_button(self):
        self.find_element(*self.locator.CONTINUE).click()

    def click_help_button(self):
        self.find_element(*self.locator.HELP).click()

    def click_signin_button(self):
        self.find_element(*self.locator.SIGNIN).click()

    def click_forgot_pass_link(self):
        self.find_element(*self.locator.FORGOTPASS).click()

    def click_other_issues_link(self):
        self.find_element(*self.locator.OTHERISSUES).click()
