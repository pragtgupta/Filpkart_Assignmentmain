from selenium.webdriver.common.by import By

from Locators.AllLocators import alllocators


class logout():

    def __init__(self, driver):
        self.driver = driver
    def myprofile(self):
        self.profile = self.driver.find_element(By.XPATH, alllocators.Myprofile)
        return self.profile.click()
    def clicklogout(self):
        self.log=self.driver.find_element(By.XPATH,alllocators.logout)
        return self.log.click()