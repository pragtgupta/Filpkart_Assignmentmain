from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Locators.AllLocators import alllocators


class searchandaddfilter():

    def __init__(self, driver):
        self.driver = driver
    def Morebrand(self):
        self.more=self.driver.find_element(By.XPATH, alllocators.moreoption)
        self.more.click()
    def selectmore(self,value):
        self.moreoption=self.driver.find_element(By.XPATH,alllocators.moreoptionsearch)
        self.moreoption.click()
        self.moreoption.send_keys(value)
    def iterateoverbrand(self):
        self.brandlist=self.driver.find_elements(By.XPATH,alllocators.listofbrand)
        return self.brandlist
    def displayedbrand(self):
        self.displaybrand=self.driver.find_elements(By.XPATH,alllocators.listofbrandlist)
        return self.displaybrand
