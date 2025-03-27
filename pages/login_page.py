from selenium.common import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):

    url = "https://kuboteka.shop/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    info_close = "//span[@class='close']"
    personal_account = "//a[@class='header__info__item__icon']"
    user_name = "//input[@id='input-email']"
    password = "//input[@id='input-password']"
    login_button = "//input[@class='btn__default btn__yellow btn__myaccount__login']"
    main_word = "//h1[@class='title__x title__x--myaccount']"

    # Getters

    def get_info_close(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.info_close)))

    def get_personal_account(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.personal_account)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_info_close(self):
        self.get_info_close().click()
        print("Click Info Close")

    def click_personal_account(self):
        self.get_personal_account().click()
        print("Click Personal Account")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input User Name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login Button")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        try:
            self.click_info_close()
        except TimeoutException as exception:
            print("The information banner was not found")
        self.click_personal_account()
        self.input_user_name("delbogdan@yandex.ru")
        self.input_password("Zz123456@")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Личный кабинет")
