from calendar import c
import time
from tests.base_test import BaseTest
from pages.homePage import HomePage
from utils import users
from utils.test_cases import test_cases


class TestCareersPage(BaseTest):
    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = HomePage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_navigation_careers_page(self):
        print("\n" + str(test_cases(4)))
        page = HomePage(self.driver)
        careers_page = page.navigate_careers_page()
        self.assertIn("amazon.jobs/en-gb/", careers_page.get_url())

    def test_search_job(self):
        print("\n" + str(test_cases(10)))
        page = HomePage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 4700);")
        time.sleep(1)
        careersPage = page.navigate_careers_page()
        careersPage.enter_name_job('Software')
        careersPage.enter_location_job('Canada')
        careersPage.find_job_button()
        time.sleep(1)
        careersPage.saveScreenShoot("job_rearch_results.png")

        softwareText = careersPage.get_text_result()
        self.assertIsNotNone(softwareText)
        return careersPage

    def test_xapply_job_with_parttime(self):
        print("\n" + str(test_cases(11)))

        careersPage = self.test_search_job()
        self.driver.execute_script("window.scrollTo(0, 300);")
        careersPage.checked_box_parttime()
        time.sleep(1)
        careersPage.saveScreenShoot("job_rearch_results2.png")
        careersPage.detail_job()
        careersPage.click_apply_button()

        loginPage = careersPage.click_login_link()

        user = users.statusUser("login")
        loginPage.enter_email(user["email"])
        loginPage.enter_password(user["password"])
        loginPage.click_signin_button()

        time.sleep(1)
        careersPage.saveScreenShoot("after_apply_job.png")
        self.assertIn('s', careersPage.get_url())
