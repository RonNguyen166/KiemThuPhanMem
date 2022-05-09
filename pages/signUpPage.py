from pages.homePage import *
from utils.locators import *
from pages.basePage import BasePage
from utils import users


class SignUpPage(BasePage):
    def __init__(self, driver):
        self.locator = SignUpPageLocators
        super().__init__(driver)

    def enter_username(self, username):
        self.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def enter_passwordConfirm(self, passwordConfirm):
        self.find_element(
            *self.locator.PASSWORDCONFIRM).send_keys(passwordConfirm)

    def click_SignUp_button(self):
        self.find_element(*self.locator.SUBMIT).click()

    def alert_message(self, element):
        if element == "username":
            return self.find_element(*self.locator.ALERT_ERROR_USERNAME).text
        elif element == "email":
            return self.find_element(*self.locator.ALERT_ERROR_EMAIL).text
        else:
            return self.find_element(*self.locator.AlERT_ERROR_PASSWORD).text

    def signup(self, status):
        user = users.statusUser(status)
        self.enter_username(user["username"])
        self.enter_email(user["email"])
        self.enter_password(user["password"])
        self.enter_passwordConfirm(user["passwordCheck"])
        self.click_SignUp_button()

    def signup_user(self, user):
        self.signup(user)
        return SignUpPage(self.driver)
