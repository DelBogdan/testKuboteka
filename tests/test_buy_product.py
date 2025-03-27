import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage


"""Тестирование покупки товара"""
@pytest.mark.run(order=2)
def test_buy_product(set_up):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    login = LoginPage(driver)
    login.authorization()

    cp = CatalogPage(driver)
    cp.select_product()

    cart_page = CartPage(driver)
    cart_page.cart()

    f = FinishPage(driver)
    f.finish()

    driver.quit()