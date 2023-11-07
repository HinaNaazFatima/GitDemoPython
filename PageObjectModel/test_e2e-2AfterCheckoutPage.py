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
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Test_one(BaseClass):

    def test_e2e(self,setup):
        homepage=HomePage(self.driver)
        homepage.ShopItems().click()
                #  //a[contains(@href,'shop')]    a[href*='shop']
        #self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        #products = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")

        checkoutPage=CheckOutPage(self.driver)
        products = checkoutPage.getcardTitles()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                #checkoutPage.getCardFooter().click()

        self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        #self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        checkoutPage.getCheckOut().click()
        self.driver.find_element(By.ID,"country").send_keys("ind")
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        time.sleep(10)
        successText = self.driver.find_element(By.CLASS_NAME,"alert-success").text
        assert "Success! Thank you!" in successText
        #self.driver.close()




















