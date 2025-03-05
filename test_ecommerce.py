from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageobjects.shopClass import Shop


def test_e2ecommoerce(browserInvokation):
    driver, wait=browserInvokation
    driver.get('https://rahulshettyacademy.com/angularpractice/')

    endtoend = Shop(driver, wait)
    endtoend.Shopit()
