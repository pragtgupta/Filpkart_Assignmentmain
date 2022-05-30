from selenium.webdriver.common.by import By

from Locators.AllLocators import alllocators


class manageaddress():

    def __init__(self, driver):
        self.driver = driver
    def clickonmagegeadd(self):
        self.mangaddres = self.driver.find_element(By.XPATH, alllocators.clickonmangeadd)
        return self.mangaddres.click()
    def addnewaddress(self):
        self.newadd=self.driver.find_element(By.XPATH,alllocators.addnewaddress)
        return self.newadd.click()
    def nameee(self,value):
        self.nam=self.driver.find_element(By.XPATH,alllocators.Name)
        return self.nam.send_keys(value)
    def mobileno(self,value):
        self.mobno=self.driver.find_element(By.XPATH,alllocators.Mobilenumber)
        return self.mobno.send_keys(value)
    def pincode(self,value):
        self.mobno=self.driver.find_element(By.XPATH,alllocators.pincode)
        return self.mobno.send_keys(value)
    def Locality(self,value):
        self.mobno=self.driver.find_element(By.XPATH,alllocators.Locality)
        return self.mobno.send_keys(value)
    def Address(self,value):
        self.mobno=self.driver.find_element(By.XPATH,alllocators.Address)
        return self.mobno.send_keys(value)
    def clearcity(self):
        self.clearchit=self.driver.find_element(By.XPATH,alllocators.cityedit)
        return self.clearchit.clear()
    def city(self,value):
        self.mobno=self.driver.find_element(By.XPATH,alllocators.city)
        return self.mobno.send_keys(value)
    def stateclick(self):
        self.mobno=self.driver.find_element(By.XPATH,alllocators.state)
        return self.mobno.click()
    # edit sta as its dropdown
    def selectstate(self):
        self.mobno=self.driver.find_elements(By.XPATH,alllocators.state1)
        return self.mobno
    def work(self):
        self.mobno=self.driver.find_element(By.XPATH,alllocators.work)
        return self.mobno.click()
    def savebut(self):
        self.sav=self.driver.find_element(By.XPATH,alllocators.Save)
        return self.sav.click()
    def city(self, value):
        self.mobno = self.driver.find_element(By.XPATH, alllocators.city)
        return self.mobno.send_keys(value)



