import unittest
from tests.base_test import BaseTest
from pages.homePage import *
from utils.test_cases import test_cases
import time

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>


class TestHomePage(BaseTest):

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = HomePage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_search_item(self):
        print("\n" + str(test_cases(1)))
        page = HomePage(self.driver)

        page.saveScreenShoot('BeforeSearch.png')
        search_result = page.search_item("Iphone 12")
        page.saveScreenShoot('AfterSearch.png')

        self.assertIn("iPhone 12", search_result)

    def test_sign_up_button(self):
        print("\n" + str(test_cases(2)))
        page = HomePage(self.driver)
        sign_up_page = page.click_sign_up_button()
        self.assertIn("ap/register", sign_up_page.get_url())

    def test_sign_in_button(self):
        print("\n" + str(test_cases(3)))
        page = HomePage(self.driver)
        login_page = page.click_sign_in_button()
        self.assertIn("ap/signin", login_page.get_url())

    def test_careers_page(self):
        print("\n" + str(test_cases(4)))
        page = HomePage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 5100);")
        careers_page = page.navigate_careers_page()

        self.assertIn("www.amazon.jobs", careers_page.get_url())
