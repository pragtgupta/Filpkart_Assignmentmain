from selenium.webdriver.common.by import By

from Locators.AllLocators import alllocators
from selenium.webdriver.common.keys import Keys

class cartfunctionality():

    def __init__(self, driver):
        self.driver = driver

    def searchproduct(self,value):
        self.prod=self.driver.find_element(By.XPATH, alllocators.searchbutton)
        self.prod.click()
        self.prod.send_keys(value,Keys.ENTER)
    def selectfirstprod(self,num):
        if num==1:
            self.selectprd=self.driver.find_element(By.XPATH,alllocators.fistmobile)
        elif num==2:
            self.selectprd = self.driver.find_element(By.XPATH, alllocators.firstshirt)
        else:
            self.selectprd=self.driver.find_element(By.XPATH,alllocators.firstwashingmachines)
        self.selectprd.click()
    def addtocart(self):
        self.add=self.driver.find_element(By.XPATH,alllocators.addtocart)
        self.add.click()
    def addpincode(self,value):
        self.pin=self.driver.find_element(By.XPATH,alllocators.pincode)
        self.pin.clear()
        self.pin.send_keys(value,Keys.ENTER)
    def selectsihirtsize(self):
        self.size=self.driver.find_element(By.XPATH,alllocators.shirtsize)
        self.size.click()
    def storethevalue(self):
        self.var=self.driver.find_element(By.XPATH,alllocators.text)
        return self.var.text
    def storethevalueforshirt(self):
        self.tex=self.driver.find_element(By.XPATH,alllocators.shirttext)
        return self.tex.text
    def storevalueforwashing(self):
        self.was=self.driver.find_element(By.XPATH,alllocators.washingmachintext)
        return  self.was.text
    def checkthecart(self):
        self.cardcheck=self.driver.find_elements(By.XPATH,alllocators.cart)
        return self.cardcheck