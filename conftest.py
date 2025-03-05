import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Add CLI option for browser selection
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose browser: chrome, firefox, edge, brave"
    )

@pytest.fixture(scope="function")
def browserInvokation(request):
    browser_name = request.config.getoption("--browser_name")  # Get browser name from CLI

    if browser_name == "chrome":
        driver = webdriver.Chrome()  # Chrome driver
    elif browser_name == "firefox":
        driver = webdriver.Firefox()  # Firefox driver
    elif browser_name == "edge":
        driver = webdriver.Edge()  # Edge driver
    elif browser_name == "brave":
        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Brave path
        options = webdriver.ChromeOptions()  # Use Chrome options
        options.binary_location = brave_path  # Set Brave as binary
        driver = webdriver.Chrome(options=options)  # Brave uses Chrome driver
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")  # Handle invalid browser

    driver.implicitly_wait(3)  # Implicit wait for 3 sec
    wait = WebDriverWait(driver, 10)  # Explicit wait for 10 sec
    yield driver, wait  # Return driver & wait for tests

    driver.quit()  # Close browser after test
