import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    last_name = "//input[@id='customer_lastname']"
    first_name = "//input[@id='customer_firstname']"
    telephone = "//input[@id='customer_telephone']"
    payment_and_delivery = "//input[@id='payment_address_deferredField_0']"
    delivery = "//input[@id='pickup.pickup']"
    confirm_button = "//input[@id='button-confirm']"

    # Getters

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_payment_and_delivery(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.payment_and_delivery)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    # Actions

    def input_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_telephone(self, telephone):
        self.get_telephone().send_keys(telephone)
        print("Input telephone")

    def click_payment_and_delivery(self):
        self.get_payment_and_delivery().click()
        print("Click payment and delivery")

    def click_delivery(self):
        self.get_delivery().click()
        print("Click delivery")

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("Click confirm button")

    # Methods

    def finish(self):
        self.get_current_url()
        self.input_last_name("Дель")
        self.input_first_name("Богдан")
        self.input_telephone("+7(952)105-64-77")
        self.click_payment_and_delivery()
        self.click_delivery()
        self.click_confirm_button()
        self.assert_finish_url("https://securepayments.tinkoff.ru")
        time.sleep(3)
        self.get_screenshot("Finish_")
