import time
from tests.base_test import BaseTest
from pages.homePage import *
from utils.test_cases import test_cases
from utils import users


class TestDetailPage(BaseTest):

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = HomePage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_search_item(self):
        print("\n" + str(test_cases(1)))
        page = HomePage(self.driver)
        page.saveScreenShoot('pre_item.png')
        search_result = page.search_item("iPhone 12")
        self.assertIn("iPhone", search_result)
        page.saveScreenShoot('pro_item.png')
        return page.detail_item()

    def test_search_item_add_to_card(self):
        print("\n" + str(test_cases(8)))
        item = self.test_search_item()
        item.click_add_to_card_button()

        item.saveScreenShoot('item_add_cart.png')
        self.assertIn("/cart", item.get_url())

    def test_search_item_to_buy(self):
        print("\n" + str(test_cases(9)))
        item = self.test_search_item()

        item.click_buy_button()
        user = users.statusUser("login")
        item.enter_email(user["email"])
        item.click_continue_button()
        item.enter_pass(user["password"])
        item.click_singin_button()
        item.enter_phone("0123456789")
        item.enter_address1("Vietnam General Delivery")
        item.enter_address2("Vietnam General Delivery")
        item.enter_city("Da Nang")

        item.enter_zipcode("1234")
        item.click_default_address_checkbox()

        item.click_submit_address_button()
        time.sleep(2)
        item.saveScreenShoot('item_to_buy.png')
        self.assertIn("gp/buy", item.get_url())

    def test_search_item_with_qty_add_to_card(self):
        print("\n" + str(test_cases(8)))
        item = self.test_search_item()

        select = item.click_select_qty()
        select.select_by_index(2)

        item.click_add_to_card_button()

        msg = item.msg_check_value()
        self.assertIn("3", msg)
        item.saveScreenShoot('item_add_cart.png')
        self.assertIn("/cart", item.get_url())
