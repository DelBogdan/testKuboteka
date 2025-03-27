import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    coupon_send = "//input[@id='coupon-send']"
    coupon_send_enter_button = "//span[@class='coupon-btn']"
    info_wrong_coupon_send = "//p[contains(text(), 'Не получилось')]"
    confirm_button = "//a[@id='button-confirm']"
    cart_word = "(//div[@class='checkout-heading panel-heading'])[2]"
    clear_cart = "(//span[@class='top__cart__clear'])[1]"
    popup_yes = "//a[@class='btn__yellow btn-popup']"
    update_cart_button = "//button[@class='btn__default btn__yellow btn__myaccount__login']"

    # Getters

    def get_coupon_send(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.coupon_send)))

    def get_coupon_send_enter_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.coupon_send_enter_button)))

    def get_info_wrong_coupon_send(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.info_wrong_coupon_send)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_clear_cart(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.clear_cart)))

    def get_popup_yes(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_yes)))

    def get_update_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.update_cart_button)))

    # Actions

    def input_coupon_send(self):
        self.get_coupon_send().send_keys("test")
        print("Input coupon send")

    def click_coupon_send_enter_button(self):
        self.get_coupon_send_enter_button().click()
        print("Click coupon send enter button")

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("Click confirm button")

    def click_clear_cart(self):
        try:
            self.get_clear_cart().click()
            print("Click clear cart")
            self.click_popup_yes()
        except TimeoutException as exception:
            print("Корзина пуста!")

    def click_popup_yes(self):
        self.get_popup_yes().click()
        print("Click popup yes")

    def click_update_cart_button(self):
        self.get_update_cart_button().click()
        print("Click update cart button")

    # Methods

    """Проверка корзины и проверка применения скидочного купона(негативное)"""
    def cart(self):
        self.get_current_url()
        self.input_coupon_send()
        self.click_coupon_send_enter_button()
        self.assert_word(self.get_info_wrong_coupon_send(), "Не получилось :(")
        self.click_update_cart_button()
        time.sleep(3)
        self.click_confirm_button()
        self.assert_word(self.get_cart_word(), "3. Способ доставки")

    """Очистка корзины"""
    def cart_clear(self):
        self.get_current_url()
        self.click_clear_cart()
        time.sleep(3)
        self.get_screenshot("Empty cart_")



