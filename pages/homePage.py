from selenium.webdriver.common.keys import Keys
from pages.basePage import BasePage
from utils.locators import MainPageLocators
from pages.signUpPage import SignUpPage
from pages.detailPage import DetailPage
from pages.careersPage import CareersPage


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators()
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO)else False

    def click_sign_in_button(self):
        self.find_element(*self.locator.LOGIN).click()
        return SignUpPage(self.driver)

    def click_sign_up_button(self):
        self.find_element(*self.locator.SIGNUP).click()
        return SignUpPage(self.driver)

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        return self.find_element(*self.locator.SEARCH_LIST).text

    def detail_item(self):
        self.find_element(*self.locator.ITEM_LINK).click()
        return DetailPage(self.driver)

    def navigate_careers_page(self):
        self.find_element(*self.locator.CAREERS_LINK).click()
        return CareersPage(self.driver)
