#imported Locators from previous package
import time
import pytest
from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObjectModel.CheckoutPage import CheckOutPage
from PageObjectModel.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass



class TestHomepage(BaseClass):

    def test_formSubmission(self,getData):
        #service_obj = Service("C:/Users/hinan/OneDrive/Documents/chromedriver.exe")
        #driver = webdriver.Chrome(service=service_obj)
        #driver.maximize_window()
        #driver.get("https://rahulshettyacademy.com/angularpractice/")

        # ID,Xpath, CSSSelector, Classname,name,linktext
        # self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
        homepage=HomePage(self.driver)
        homepage.getName().send_keys(getData["FirstName"])
        homepage.getEmail().send_keys(getData["Email"])
        #self.driver.find_element(By.NAME, "email").send_keys("hinafatima@gmail.com")
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("qwerty34")
        homepage.getCheckBox().click()
        #self.driver.find_element(By.ID, "exampleCheck1").click()

        #dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        #dropdown.select_by_visible_text("male")
        self.selectOptionsByText(homepage.getGender(),getData["Gender"])
        #dropdown.select_by_index(0)
        #homepage.getGender().send_keys("male")
        # CSS- tagname[attribute='value']->input[type='submit'], #id,.classname
        # XPath- //tagname[@attribute='value']->//input[@type='submit']

        self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        homepage.submitForm().click()
        #message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        message=homepage.getSuccessMessage().text
        print(message)
        assert "Success" in message
        time.sleep(3)
        self.driver.refresh()

        #self.driver.close()

    @pytest.fixture(params=HomePageData.test_HomePageData)
    def getData(self,request):
        return request.param