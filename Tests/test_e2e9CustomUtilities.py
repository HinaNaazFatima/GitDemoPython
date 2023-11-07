import time

import pytest
from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class Test_one(BaseClass):
    def test_e2e(self):

        #  //a[contains(@href,'shop')]    a[href*='shop']
        log=self.getLogger()
        self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        products = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")
        log.info("Getting the info")
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":

                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID,"country").send_keys("ind")
        log.info("entering country name as india")
        #wait = WebDriverWait(self.driver,10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.VerifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        time.sleep(10)
        successText = self.driver.find_element(By.CLASS_NAME,"alert-success").text
        log.info("text received from application"+successText)
        assert "Success! Thank you!" in successText
        #self.driver.close()




















