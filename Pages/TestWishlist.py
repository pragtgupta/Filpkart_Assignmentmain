from selenium.webdriver.common.by import By

from Locators.AllLocators import alllocators


class wishlist():

    def __init__(self, driver):
        self.driver = driver
    def howeroverfasion(self):
        self.hower=self.driver.find_element(By.XPATH, alllocators.fasionsection)
        return self.hower
    def menstopwear(self,val):
        if val==1:
            self.wear=self.driver.find_element(By.XPATH,alllocators.Menstopwear)
            return self.wear
    def subsection(self,val):
        if val == 1:
            self.subsec=self.driver.find_element(By.XPATH,alllocators.menstshirt)
            return self.subsec.click()
        elif val==2:
            self.subsec = self.driver.find_element(By.XPATH, alllocators.womensare)
            return self.subsec.click()
    def womenethenic(self):
        self.wear = self.driver.find_element(By.XPATH, alllocators.Womenehenic)
        return self.wear
    def addfirstsare(self):
        self.sare=self.driver.find_element(By.XPATH,alllocators.firstsaree)
        return self.sare.click()
    def addtowishlist(self):
        self.wish=self.driver.find_element(By.XPATH,alllocators.addtowish)
        return self.wish.click()
    def clickhomepage(self):
        self.home=self.driver.find_element(By.XPATH,alllocators.homepage)
        return self.home.click()
    def myprofile(self):
        self.profie=self.driver.find_element(By.XPATH,alllocators.profile)
        return self.profie
    def clickonwishlist(self):
        self.clickwishlist=self.driver.find_element(By.XPATH,alllocators.wishlistpage)
        return self.clickwishlist.click()
    def wishlistitems(self):
        self.wishlistitemlist=self.driver.find_elements(By.XPATH,alllocators.wishlistitem)
        return self.wishlistitemlist
    def storeprdtext(self):
        self.text=self.driver.find_element(By.XPATH,alllocators.producttext)
        return self.text
