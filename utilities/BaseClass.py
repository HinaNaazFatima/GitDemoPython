import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfile2.log")
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object\
        logger.setLevel(logging.INFO)
        return logger
    def VerifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))
        self.driver.find_element(By.LINK_TEXT, text)

    def selectOptionsByText(self,locator,text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)