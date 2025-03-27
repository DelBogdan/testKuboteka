import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage

"""Тестирование добавление товара в избранное"""
@pytest.mark.run(order=3)
def test_add_to_favorites(set_up):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    login = LoginPage(driver)
    login.authorization()

    cp = CatalogPage(driver)
    cp.add_favorites_and_check()

    driver.quit()


