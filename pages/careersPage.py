from pages.basePage import BasePage
from pages.loginPage import LoginPage
from utils.locators import CareersPageLocators


class CareersPage(BasePage):
    def __init__(self, driver):
        self.locator = CareersPageLocators
        super().__init__(driver)  # Python2 version

    def enter_name_job(self, name):
        self.find_element(*self.locator.FINDNAME).send_keys(name)

    def enter_location_job(self, location):
        self.find_element(*self.locator.FINDLOCATION).send_keys(location)

    def find_job_button(self):
        self.find_element(*self.locator.SEARCHBUTTON).click()

    def detail_job(self):
        self.find_element(*self.locator.DETAILJOB).click()

    def checked_box_parttime(self):
        self.find_element(*self.locator.CHECKBOXPARTTIME).click()

    def click_apply_button(self):
        self.find_element(*self.locator.APPLYBUTTON).click()

    def click_login_link(self):
        self.find_element(*self.locator.LOGIN).click()
        return LoginPage(self.driver)

    def get_text_result(self):
        return self.find_element(*self.locator.SOFTWARETEXT)
