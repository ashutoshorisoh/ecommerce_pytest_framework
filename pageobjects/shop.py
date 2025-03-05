from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class Shop:
    def __init__(self, driver, wait):
        self.shopbtn = (By.XPATH, "//a[normalize-space()='Shop']")
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.checkOutBtn = (By.XPATH, "//a[contains(text(), 'Checkout')]")
        self.finalCheckOutBtn = (By.XPATH, "//button[contains(text(), 'Checkout')]")
        self.countryInput = (By.XPATH, "//input[@id='country']")
        self.termsAgree = (By.XPATH, "//label[@for='checkbox2']")
        self.purchaseClick = (By.XPATH, "//input[@value='Purchase']")
        self.successMessage = (By.XPATH, "//strong[normalize-space()='Success!']")
        self.driver = driver
        self.wait = wait

    def go_to_shoping_page(self):
        self.driver.find_element(*self.shopbtn).click()

    def pick_products(self, product_name):
        products = self.driver.find_elements(*self.products)
        for product in products:
            title = product.find_element(By.XPATH, "div/h4/a")
            if title.text == product_name:
                checkOut = product.find_element(By.XPATH, "div/button")
                checkOut.click()
                break

    def checkout(self):
        self.driver.find_element(*self.checkOutBtn).click()
        self.driver.find_element(*self.finalCheckOutBtn).click()

    def address_and_purchase(self, country_name):
        self.driver.find_element(*self.countryInput).send_keys("Ind")

        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, f"//div[@class='suggestions']/ul/li/a[contains(text(), '{country_name}')]")))
        country_select = self.driver.find_element(By.XPATH, f"//div[@class='suggestions']/ul/li/a[contains(text(), '{country_name}')]")
        country_select.click()

        self.driver.find_element(*self.termsAgree).click()
        self.driver.find_element(*self.purchaseClick).click()

    def success_message(self):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.successMessage))
        assert element.is_displayed(), "Error: Success message not displayed"
