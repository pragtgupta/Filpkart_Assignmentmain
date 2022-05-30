import time

from selenium.webdriver.common.by import By

from Locators.AllLocators import alllocators
from Pages.Loginpage import loginpages
from Pages.TestCartFunctionality import cartfunctionality
from Pages.TestSearchandFilter import searchandaddfilter
from Utilities import XLUtilities
from Utilities.Customelogger import loggings
from Utilities.readproprties import readconfig


class Test_001_cartfunction:
    path = "/Users/sikalidas/PycharmProjects/FlipkartProject_Main/TestData/Userdetails.xlsx"

    URL = XLUtilities.readData(path, 'Sheet3', 2, 2)
    usernamee = XLUtilities.readData(path, 'Sheet2', 2, 1)
    Password = XLUtilities.readData(path, 'Sheet2', 2, 2)
    logeer = loggings.loggen()
    searchprod = XLUtilities.readData(path, 'Sheet4', 5, 2)
    brand=XLUtilities.readData(path, 'Sheet4', 6, 2)
    global my_list
    my_list = []
    global my_list1
    my_list1 = []

    def test_Addproducts(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.key = loginpages(self.driver)
        self.key.setusername(self.usernamee)
        self.key.setpassword(self.Password)
        self.key.clicklogin()
        time.sleep(10)
        self.key1 = cartfunctionality(self.driver)
        self.key1.searchproduct(self.searchprod)
        time.sleep(10)
        self.key2=searchandaddfilter(self.driver)
        self.key2.Morebrand()
        time.sleep(10)
        self.key2.selectmore(self.brand)
        time.sleep(10)
        tempp=self.key2.iterateoverbrand()
        print(len(tempp))
        for item in tempp:
            ref=item.text
            my_list.append(item.text)
            if ref.lower() == self.brand:
                self.driver.find_element(By.XPATH,alllocators.listofbrand).click()
                time.sleep(10)
                self.driver.find_element(By.XPATH,alllocators.clickonapply).click()
                break
        time.sleep(10)
        listm=self.key2.displayedbrand()
        vari=0
        for item2 in listm:
            ref=item2.text
            my_list1.append(item2.text)
        for item in my_list:
            for item1 in my_list1:
                if item1.startswith(item):
                   vari=1
        if vari==1:
            assert True
        else:
            self.driver.save_screenshot(".//Screenshort//" + "Test_001_searchandfilter.png")
            assert False

