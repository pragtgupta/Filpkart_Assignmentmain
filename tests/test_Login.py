import time

from selenium.webdriver.chrome import webdriver

from Locators import AllLocators
from Locators.AllLocators import alllocators

from Pages.Loginpage import loginpages
from Utilities import XLUtilities
from Utilities.Datadriven import data
from Utilities.readproprties import readconfig
from Utilities.Customelogger import loggings

class Test_001_homepage:
    path = "/Users/sikalidas/PycharmProjects/FlipkartProject_Main/TestData/Userdetails.xlsx"

    URL=XLUtilities.readData(path, 'Sheet3', 2, 2)
    usernamee=XLUtilities.readData(path, 'Sheet2', 2, 1)
    Password=XLUtilities.readData(path, 'Sheet2', 2, 2)
    logeer=loggings.loggen()
    title=XLUtilities.readData(path, 'Sheet3', 3, 2)
    usertitle=XLUtilities.readData(path, 'Sheet3', 4, 2)
    grosariestitle=XLUtilities.readData(path, 'Sheet3', 5, 2)


    def test_homepage(self,setup):
        self.logeer.info("***********test_homepage****************")
        self.logeer.info("**********Verifying Homepage************")
        self.driver = setup
        self.driver.get(self.URL)
        titles = self.driver.title
        if self.title == titles:
            assert True
        else:
            assert False
        self.driver.close()
        self.logeer.info("*************************Home page is verified **************")
    def test_loginpage(self,setup):
        self.driver=setup
        self.driver.get(self.URL)
        self.key=loginpages(self.driver)
        self.key.setusername(self.usernamee)
        self.key.setpassword(self.Password)
        self.key.clicklogin()
        time.sleep(10)
        temp=self.key.getusertitle()
        if temp==self.usertitle:
            assert True
        else:
            self.driver.save_screenshot(".//Screenshort//" + "test_loginpage.png")
            assert False
        self.key.clickongrocery()
        time.sleep(10)
        title=self.driver.title
        if title!=self.grosariestitle:
            self.driver.save_screenshot(".//Screenshort//" + "test_loginpage1.png")
            assert title==self.grosariestitle
        self.driver.close()
