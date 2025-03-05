from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageobjects.Login import Login
from pageobjects.shop import Shop


def test_e2ecommoerce(browserInvokation):
    driver, wait=browserInvokation
    driver.get('https://rahulshettyacademy.com/loginpagePractise/')

    login= Login(driver,wait)
    shopPage=login.login("rahulshettyacademy", "learning")
    shopPage.go_to_shoping_page()
    shopPage.pick_products("Blackberry")
    shopPage.checkout()
    shopPage.address_and_purchase("India")
    shopPage.success_message()

