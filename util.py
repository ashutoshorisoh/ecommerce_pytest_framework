class Browser:
    def __init__(self, driver):
        self.driver=driver

    def getBrowserTitle(self):
        return self.driver.title