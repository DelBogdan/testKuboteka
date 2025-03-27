import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage


"""Тестирование очистки корзины"""
@pytest.mark.run(order=1)
def test_buy_product(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    login = LoginPage(driver)
    login.authorization()

    cp = CatalogPage(driver)
    cp.select_cart()

    cart_page = CartPage(driver)
    cart_page.cart_clear()

    driver.quit()


