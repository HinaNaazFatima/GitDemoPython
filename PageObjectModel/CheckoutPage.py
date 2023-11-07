from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver=driver

    #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    CardTitle = (By.XPATH, "//div[@class='card h-100']")
    #product.find_element(By.XPATH, "div/button").click()
    CardFooter = (By.XPATH, "div/button")

    def getcardTitles(self):
        return self.driver.find_elements(*CheckOutPage.CardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.CardFooter)

    #self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
    CheckOut=(By.XPATH,"//button[@class='btn btn-success']")
    def getCheckOut(self):
        return self.driver.find_element(*CheckOutPage.CheckOut)