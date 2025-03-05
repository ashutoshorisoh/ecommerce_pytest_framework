from selenium.webdriver.common.by import By

from pageobjects.shop import Shop


class Login:
    def __init__(self, driver, wait):
        self.driver=driver
        self.wait=wait
        self.username_input=(By.ID, "username")
        self.password_input=(By.ID, "password")
        self.terms= (By.ID, "terms")
        self.submit=(By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.terms).click()
        self.driver.find_element(*self.submit).click()

        return Shop(self.driver, self.wait)
