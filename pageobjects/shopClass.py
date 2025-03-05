from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Shop:
    def __init__(self,driver,wait):
        self.shopbtn = (By.XPATH, "//a[normalize-space()='Shop']")
        self.products= (By.XPATH, "//div[@class='card h-100']")
        self.checkOutBtn = (By.XPATH, "//a[contains(text(), 'Checkout')]")
        self.finalCheckOutBtn = (By.XPATH, "//button[contains(text(), 'Checkout')]")
        self.countryInput = (By.XPATH, "//input[@id='country']")
        self.countrySelect= (By.XPATH, "//div[@class='suggestions']/ul/li/a[contains(text(),'India')]")
        self.termsAgree = (By.XPATH, "//label[@for='checkbox2']")
        self.purchaseClick = (By.XPATH, "//input[@value='Purchase']")
        self.successMessage = (By.XPATH, "//div/strong")
        self.driver=driver
        self.wait=wait

    def Shopit(self):
        self.driver.find_element(*self.shopbtn).click()

        products = self.driver.find_elements(*self.products)

        for product in products:
            title = product.find_element(By.XPATH, "div/h4/a")
            if title.text == "Blackberry":
                checkOut = product.find_element(By.XPATH, "div/button")
                checkOut.click()
                break

        self.driver.find_element(*self.checkOutBtn).click()

        self.driver.find_element(*self.finalCheckOutBtn).click()

        self.driver.find_element(*self.countryInput).send_keys("Ind")

        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//div[@class='suggestions']/ul/li/a[contains(text(),'India')]")))
        country_select = self.driver.find_element(By.XPATH, "//div[@class='suggestions']/ul/li/a[contains(text(),'India')]")
        country_select.click()

        self.driver.find_element(*self.termsAgree).click()

        self.driver.find_element(* self.purchaseClick).click()

        element = self.wait.until(expected_conditions.visibility_of_element_located(self.successMessage))

        assert element.is_displayed(), "error is succes message"

