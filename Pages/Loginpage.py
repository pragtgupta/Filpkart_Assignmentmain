from selenium.webdriver.common.by import By

from Locators.AllLocators import alllocators




class loginpages():

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.user = self.driver.find_element(By.XPATH, alllocators.username2)
        self.user.click()
        self.user.send_keys(username)

    def setpassword(self, password):
        self.passs = self.driver.find_element(By.XPATH, alllocators.password)
        self.passs.click()
        self.passs.send_keys(password)

    def clicklogin(self):
        self.log = self.driver.find_element(By.XPATH, alllocators.Loginbutton)
        self.log.click()
    def getusertitle(self):
        self.usertitle=self.driver.find_element(By.XPATH,alllocators.usertitle)
        return self.usertitle.text
    def clickongrocery(self):
        self.grs=self.driver.find_element(By.XPATH,alllocators.grocery)
        self.grs.click()

