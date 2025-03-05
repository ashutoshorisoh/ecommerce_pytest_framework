import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import pytest

from pageobjects.Login import Login
from pageobjects.shop import Shop

test_data_path='data/test_ecommerce.json'
with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]

@pytest.mark.parametrize("test_data_item", test_list)
def test_e2ecommoerce(browserInvokation, test_data_item):
    driver, wait=browserInvokation
    driver.get('https://rahulshettyacademy.com/loginpagePractise/')

    login= Login(driver,wait)
    shopPage=login.login(test_data_item["username"], test_data_item["password"])
    shopPage.go_to_shoping_page()
    shopPage.pick_products(test_data_item["product_name"])
    shopPage.checkout()
    shopPage.address_and_purchase("India")
    shopPage.success_message()

