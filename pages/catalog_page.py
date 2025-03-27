import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.login_page import LoginPage


class CatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_button = "//a[@class='js__btn__catalog']"
    lego_technic_button = "(//a[@class='main-category-box'])[7]"
    filter_sales = "//span[@class='ocf-value-name']"
    filter_colors = "//button[@id='ocf-v-1200-2-1861683761-1']"
    filter_status = "//button[@id='ocf-v-1-0-11-1']"
    filter_decorated = "//button[@id='ocf-v-1700-2-754528263-1']"
    show_products_button = "//button[@class='ocf-btn ocf-btn-block ocf-search-btn-static']"
    first_product_in_list = "(//button[contains(text(), 'В корзину')])[1]"
    cart = "//a[@class='header__info__item header__info__item--cart']"
    cart_word = "//h1[@class='title__x']"
    add_favorite_button = "(//a[@class='product__card__favorite'])[1]"
    article_favorite_product = "(//span[@class='product__main__characteristic__bricklink'])[1]"
    favorite_button = "(//span[@class='myaccount__menu__item__count'])[2]"
    article = "//div[@class='product__card__ref--bl']"

    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_lego_technic_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.lego_technic_button)))

    def get_filter_sales(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_sales)))

    def get_filter_colors(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_colors)))

    def get_filter_status(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_status)))

    def get_filter_decorated(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_decorated)))

    def get_show_products_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.show_products_button)))

    def get_first_product_in_list(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_product_in_list)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_add_favorite_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_favorite_button)))

    def get_article_favorite_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.article_favorite_product)))

    def get_favorite_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.favorite_button)))

    def get_article(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.article)))

    # Actions

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click Catalog Button")

    def click_lego_technic_button(self):
        self.get_lego_technic_button().click()
        print("Click lego technic button")

    def click_filter_sales(self):
        self.get_filter_sales().click()
        print("Click filter sales")

    def click_filter_colors(self):
        self.get_filter_colors().click()
        print("Click filter colors")

    def click_filter_status(self):
        self.get_filter_status().click()
        print("Click filter status")

    def click_filter_decorated(self):
        self.get_filter_decorated().click()
        print("Click filter decorated")

    def click_show_products_button(self):
        self.get_show_products_button().click()
        print("Click show products button")

    """Скролим фильтр, чтобы были кликабельны нужные атрибуты"""
    def filter_scroll_down(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_show_products_button())
        print("Scroll filter")

    def click_first_product_in_list(self):
        self.get_first_product_in_list().click()
        print("Click first product in list")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_add_favorite_button(self):
        self.get_add_favorite_button().click()
        print("Click add favorite button")

    def click_favorite_button(self):
        self.get_favorite_button().click()
        print("Click favorite button")

    def check_article(self, first, second):
        if first == second:
            print("Товар соответствует добавленному в избранное")
        else:
            print("Товар не соответствует добавленному в избранное")

    # Methods
    """Добавление товара в корзину. Использование фильтров"""
    def select_product(self):
        self.get_current_url()
        self.click_catalog_button()
        self.click_lego_technic_button()
        self.click_filter_sales()
        self.click_filter_colors()
        self.click_filter_status()
        self.filter_scroll_down()
        self.click_filter_decorated()
        self.click_show_products_button()
        self.click_first_product_in_list()
        self.click_cart()
        self.assert_url("https://kuboteka.shop/cart/")

    """Переход к корзине и проверка, что мы находимся в корзине"""
    def select_cart(self):
        self.click_cart()
        self.assert_url("https://kuboteka.shop/cart/")

    """Добавление товара в избранное и проверка товара в избранном"""
    def add_favorites_and_check(self):
        self.click_catalog_button()
        self.click_lego_technic_button()
        self.click_add_favorite_button()
        article = self.get_article_favorite_product().text
        lp = LoginPage(self.driver)
        lp.click_personal_account()
        self.click_favorite_button()
        self.check_article(article, self.get_article().text)
        time.sleep(3)
        self.get_screenshot("Favorite_")





