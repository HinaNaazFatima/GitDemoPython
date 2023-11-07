from selenium import webdriver
import time
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        service_obj = Service("C:/Users/hinan/OneDrive/Documents/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name=="firefox":
        service_obj = Service("C:/Users/hinan/OneDrive/Documents/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name=="IE":
        service_obj = Service("C:/Users/hinan/OneDrive/Documents/msedgedriver.exe")
        driver = webdriver.Ie(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver # driver is sent to class object of inherited class
    yield
    driver.close()
