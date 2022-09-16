from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.common.by import By
import time

from locators import Locators

class Registration_user():
    locators: Locators
    driver: ChromeWebDriver

    def __init__(self, locator: Locators):
        self.locators = locator

    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def successful_registration_from_lk(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.registration_button).click()
        self.driver.find_element(By.XPATH, self.locators.input_name_registration).send_keys("Katrin")
        self.driver.find_element(By.XPATH, self.locators.input_email_registration).send_keys("zaidova_k_1993@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_registration).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.registration_button).click()
        self.driver.quit()


    def failed_registration_from_log_in(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.login_button).click()
        self.driver.find_element(By.XPATH, self.locators.registration_button).click()
        self.driver.find_element(By.XPATH, self.locators.input_name_registration).send_keys("Катрин")
        self.driver.find_element(By.XPATH, self.locators.input_email_registration).send_keys("zaidova_k_1996@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_registration).send_keys("12345")
        self.driver.find_element(By.XPATH, self.locators.registration_button).click()
        self.driver.quit()

locators = Locators()
sr = Registration_user(locators)
sr.successful_registration_from_lk()
sr.failed_registration_from_log_in()

class Authorization_user():
    locators: Locators
    driver: ChromeWebDriver

    def __init__(self, locator: Locators):
        self.locators = locator

    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def authorization_from_login(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.login_button).click()
        self.driver.find_element(By.XPATH, self.locators.input_login_autorization).send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_authorization).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.come_in_button).click()
        self.driver.quit()

    def authorization_from_personal_account(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.input_login_autorization).send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_authorization).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.come_in_button).click()
        self.driver.quit()

    def authorization_from_registration_form(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.registration_button).click()
        self.driver.find_element(By.XPATH, self.locators.come_in_from_registration_and_reset_password).click()
        self.driver.find_element(By.XPATH, self.locators.input_login_authorization).send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_authorization).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.come_in_button).click()
        self.driver.quit()

    def authorization_from_reset_password(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.login_button).click()
        self.driver.find_element(By.XPATH, self.locators.reset_passwort_button).click()
        self.driver.find_element(By.XPATH, self.locators.come_in_from_registration_and_reset_password).click()
        self.driver.find_element(By.XPATH, self.locators.input_login_authorization).send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_authorization).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.come_in_button).click()
        self.driver.quit()

locators = Locators()
sr = Authorization_user(locators)
sr.authorization_from_login()
sr.authorization_from_personal_account()
sr.authorization_from_registration_form()
sr.authorization_from_reset_password()

class Page_transitions():
    locators: Locators
    driver: ChromeWebDriver


    def __init__(self, locator: Locators):
        self.locators = locator


    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://stellarburgers.nomoreparties.site/')
    def transition_on_page_personal_account(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.input_login_authorization).send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_authorization).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.come_in_button).click()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.quit()

    def transition_on_page_konstruktor_from_personal_account(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.input_login_authorization).send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_authorization).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.come_in_button).click()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.button_in_header_konstruktor).click()
        self.driver.quit()

    def transition_on_page_konstructor_if_click_on_logo_Stellar_Burgers(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.input_login_authorization).send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_authorization).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.come_in_button).click()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.logo).click()
        self.driver.quit()

    def transition_to_page_logout(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.input_login_authorization).send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_authorization).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.come_in_button).click()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.logout_button).click()
        self.driver.quit()


    def transition_from_personal_account_to_filling_sauce_hamburger_bun(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.input_login_authorization).send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, self.locators.input_password_authorization).send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, self.locators.come_in_button).click()
        self.driver.find_element(By.XPATH, self.locators.personal_account).click()
        self.driver.find_element(By.XPATH, self.locators.button_in_header_konstruktor).click()
        self.driver.find_element(By.XPATH, self.locators.fillings).click()
        self.driver.find_element(By.XPATH, self.locators.sauce).click()
        self.driver.find_element(By.XPATH, self.locators.hamburger_buns).click()
        self.driver.quit()

locators = Locators()
sr = Page_transitions(locators)
sr.transition_on_page_personal_account()
sr.transition_on_page_konstruktor_from_personal_account()
sr.transition_on_page_konstructor_if_click_on_logo_Stellar_Burgers()
sr.transition_to_page_logout()
sr.transition_from_personal_account_to_filling_sauce_hamburger_bun()
