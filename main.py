from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Registration_user():
    def __init__(self):
        self.driver = None

    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def successful_registration_from_lk(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/div/p[1]/a").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("Katrin")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("zaidova_k_1993@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.quit()


    def failed_registration_from_log_in(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[2]/div/button").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/div/p[1]/a").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("Катрин")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("zaidova_k_1996@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[3]/div/div/input").send_keys("12345")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.quit()

sr = Registration_user()
sr.successful_registration_from_lk()
sr.failed_registration_from_log_in()

class Authorization_user():
    def __init__(self):
        self.driver = None

    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def authorization_from_login(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[2]/div/button").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.quit()

    def authorization_from_personal_account(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.quit()

    def authorization_from_registration_form(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/div/p[1]/a").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/div/p/a").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.quit()

    def authorization_from_reset_password(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[2]/div/button").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/div/p[2]/a").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/div/p/a").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.quit()

sr = Authorization_user()
sr.authorization_from_personal_account()
sr.authorization_from_reset_password()

class Page_transitions():
    def __init__(self):
        self.driver = None

    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def transition_on_page_personal_account(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        time.sleep(3)
        self.driver.quit()

    def transition_on_page_konstruktor_from_personal_account(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/ul/li[1]/a/p").click()
        self.driver.quit()

    def transition_on_page_konstructor_if_click_on_logo_Stellar_Burgers(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/div/a").click()
        self.driver.quit()

    def transition_to_page_logout(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/nav/ul/li[3]/button").click()
        time.sleep(3)
        self.driver.quit()


    def transition_from_personal_account_to_filling_sauce_hamburger_bun(self):
        self.init_driver()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("zaidova_k_1995@yandex.ru")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456Qwerty!")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/ul/li[1]/a/p").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[3]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[1]").click()
        self.driver.quit()

sr = Page_transitions()
sr.transition_on_page_personal_account()
sr.transition_on_page_konstruktor_from_personal_account()
sr.transition_on_page_konstructor_if_click_on_logo_Stellar_Burgers()
sr.transition_to_page_logout()
sr.transition_from_personal_account_to_filling_sauce_hamburger_bun()
