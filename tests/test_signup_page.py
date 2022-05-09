
import time
import unittest
from tests.base_test import BaseTest

from pages.homePage import *
from utils.test_cases import test_cases


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestSignUpPage(BaseTest):

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = HomePage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_sign_up_button(self):
        print("\n" + str(test_cases(2)))
        page = HomePage(self.driver)
        sign_up_page = page.click_sign_up_button()
        self.assertIn("ap/register", sign_up_page.get_url())

    def test_sign_up_empty(self):
        print("\n" + str(test_cases(3)))
        page = HomePage(self.driver)
        sign_up_page = page.click_sign_up_button()
        sign_up_page.click_SignUp_button()
        time.sleep(1)
        alert = sign_up_page.alert_message('username')
        self.assertIn('Enter your name', alert)

    def test_sign_up_valid(self):
        print("\n" + str(test_cases(4)))
        page = HomePage(self.driver)
        signup_page = page.click_sign_up_button()
        signup_page.signup("register")
        time.sleep(1)
        self.assertIn('ap/cvf/request', page.get_url())
