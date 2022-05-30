import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.AllLocators import alllocators
from Pages.Loginpage import loginpages
from Pages.TestLogout import logout
from Pages.TestManageAddress import manageaddress
from Pages.TestWishlist import wishlist
from Utilities.Customelogger import loggings
from Utilities.readproprties import readconfig
from Utilities import XLUtilities


class Test_001_Manageaddress:
    path = "/Users/sikalidas/PycharmProjects/FlipkartProject_Main/TestData/Userdetails.xlsx"

    URL = XLUtilities.readData(path, 'Sheet3', 2, 2)
    usernamee = XLUtilities.readData(path, 'Sheet2', 2, 1)
    Password = XLUtilities.readData(path, 'Sheet2', 2, 2)
    logeer = loggings.loggen()
    path=".//TestData/Userdetails.xlsx"

    def test_Addproducts(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.key = loginpages(self.driver)
        self.key.setusername(self.usernamee)
        self.key.setpassword(self.Password)
        self.key.clicklogin()
        time.sleep(5)
        self.key2 = wishlist(self.driver)
        prf = self.key2.myprofile()
        veria = ActionChains(self.driver).move_to_element(prf)
        veria.perform()
        self.key1=logout(self.driver)
        time.sleep(5)
        self.key1.myprofile()
        self.key3=manageaddress(self.driver)
        time.sleep(20)
        prf = self.key2.myprofile()
        veria = ActionChains(self.driver).move_to_element(prf)
        veria.perform()
        self.key3.clickonmagegeadd()
        time.sleep(5)
        self.key3.addnewaddress()
        self.rw=XLUtilities.getworcount(self.path,'Sheet1')
        print(self.rw)
        self.coll=XLUtilities.getCollumcount(self.path,'Sheet1')
        print(self.coll)
        for row in range(1,self.rw+1):
            self.name = XLUtilities.readData(self.path, 'Sheet1', row, 1)
            if self.name=='Name':
                self.name1=XLUtilities.readData(self.path,'Sheet1',row,2)
            elif self.name=='Pincode':
                self.pinco=XLUtilities.readData(self.path,'Sheet1',row,2)
            elif self.name == 'phonenumber':
                self.phonenumber=XLUtilities.readData(self.path,'Sheet1',row,2)
            elif self.name == 'Locality':
                self.locality=XLUtilities.readData(self.path,'Sheet1',row,2)
            elif self.name == 'Address':
                self.Address=XLUtilities.readData(self.path,'Sheet1',row,2)
            elif self.name == 'City':
                self.City=XLUtilities.readData(self.path,'Sheet1',row,2)
            elif self.name == 'state':
                self.stateeee=XLUtilities.readData(self.path,'Sheet1',row,2)
            else:
                pass
        self.key3.nameee(self.name1)
        time.sleep(5)
        self.key3.mobileno(self.phonenumber)
        time.sleep(5)
        self.key3.pincode(self.pinco)
        time.sleep(5)
        self.key3.Locality(self.locality)
        time.sleep(5)
        self.key3.Address(self.Address)
        time.sleep(5)
        self.key3.clearcity()
        time.sleep(5)
        self.key3.city(self.City)
        time.sleep(5)
        self.key3.stateclick()
        time.sleep(5)
        select = Select(self.driver.find_element(By.XPATH,alllocators.state1))
        select.select_by_visible_text(self.stateeee)
        # print(select)
        self.key3.work()
        time.sleep(5)
        self.key3.savebut()
        time.sleep(5)
        value=self.driver.find_elements(By.XPATH,alllocators.Namefromaddress)
        count=0
        for ite in value:
            text=ite.text
            if text==self.name1:
                count=1
        if count==1:
            assert True
        else:
            self.driver.save_screenshot(".//Screenshort//" + "Test_001_Manageaddress.png")
            assert False