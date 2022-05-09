from http.client import CONTINUE
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGO = (By.ID, 'nav-logo')
    ACCOUNT = (By.ID, 'nav-link-accountList')
    SIGNUP = (By.CSS_SELECTOR, '#nav-signin-tooltip > div > a')
    LOGIN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SEARCH_LIST = (By.CSS_SELECTOR,
                   'div[data-component-type="s-search-result"]')
    ITEM_LINK = (
        By.XPATH, '//div[@data-component-type="s-search-result"]//a[@class="a-link-normal s-no-outline"]')
    HELP_LINK = (By.XPATH, '//a[text()=\'Help\']')
    CAREERS_LINK = (By.XPATH, '//a[text()=\'Careers\']')


class SignUpPageLocators():
    USERNAME = (By.ID, "ap_customer_name")
    EMAIL = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    PASSWORDCONFIRM = (By.ID, 'ap_password_check')
    SUBMIT = (By.ID, 'continue')
    ALERT_ERROR_USERNAME = (
        By.XPATH, '//*[@id="auth-customerName-missing-alert"]//div[@class="a-alert-content"]')
    ALERT_ERROR_EMAIL = (
        By.XPATH, '//*[@id="auth-email-missing-alert"]//div[@class="a-alert-content"]')
    AlERT_ERROR_PASSWORD = (
        By.XPATH, '//*[@id="auth-password-missing-alert"]//div[@class="a-alert-content"]')


class LoginPageLocators():
    EMAIL = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    CONTINUE = (By.ID, 'continue')
    SIGNIN = (By.ID, 'signInSubmit')
    REGISTER = (By.ID, 'createAccountSubmit')
    KEPPME = (
        By.XPATH, '//div[@data-a-input-name="rememberMe"]//input[@name="rememberMe"]')
    HELP = (
        By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[1]/form/div/div/div/div[3]/div/a')
    FORGOTPASS = (By.ID, 'auth-fpp-link-bottom')
    OTHERISSUES = (By.ID, 'ap-other-signin-issues-link')


class DetailPageLocators():
    ADDTOCART = (By.ID, "add-to-cart-button")
    BUYNOW = (By.ID, 'buy-now-button')
    SELECTQTY = (By.ID, 'quantity')
    MSGVALUE = (By.XPATH, '//*[@data-feature-id="proceed-to-checkout-label"]')
    EMAIL = (By.ID, 'ap_email')
    PASS = (By.ID, 'ap_password')
    CONTINUE = (By.ID, 'continue')
    SIGNIN = (By.ID, 'signInSubmit')
    LOGIN = (By.ID, 'btn-lwa-init')
    FULLNAME = (By.ID, 'address-ui-widgets-enterAddressFullName')
    PHONE = (By.ID, "address-ui-widgets-enterAddressPhoneNumber")
    ADDRESS1 = (By.ID, 'address-ui-widgets-enterAddressLine1')
    ADDRESS2 = (By.ID, 'address-ui-widgets-enterAddressLine2')
    CITY = (By.ID, 'address-ui-widgets-enterAddressCity')
    SELECTCOUNTRY = (
        By.XPATH, '//*[@id="address-ui-widgets-countryCode-dropdown-nativeId"]')
    ZIPCODE = (By.ID, 'address-ui-widgets-enterAddressPostalCode')
    CHECKBOXDEFAULT = (By.ID, 'address-ui-widgets-use-as-my-default')
    SUBMITADDRESS = (
        By.CSS_SELECTOR, '#address-ui-widgets-form-submit-button > span > input')


class CareersPageLocators():
    FINDNAME = (
        By.XPATH, "/html/body/div[2]/div[1]/div[4]/div[1]/div/div/div/div/form/div[1]/div[1]/div/span/input")
    FINDLOCATION = (
        By.XPATH, "/html/body/div[2]/div[1]/div[4]/div[1]/div/div/div/div/form/div[1]/div[2]/div/span/input")
    SEARCHBUTTON = (By.ID, "search-button")
    SOFTWARETEXT = (By.XPATH, "//h3[contains(text(),'Software')]")
    DETAILJOB = (
        By.XPATH, "//div[1][@class='job-tile']/a[contains(@href,'software')]")
    LOGIN = (By.ID, "btn-lwa-init")
    APPLYBUTTON = (By.ID, "apply-button")
    AlLOW = (
        By.XPATH, '//*[@id="lwa-aui-page-button-allow"]/span/font/font/input')
    CHECKBOXPARTTIME = (
        By.XPATH, '//*[@id="desktopFilter_job_type_filter"]/div/div/fieldset/div/button[2]')
