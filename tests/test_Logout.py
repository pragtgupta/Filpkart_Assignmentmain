import time

from selenium.webdriver import ActionChains

from Pages.Loginpage import loginpages
from Pages.TestLogout import logout
from Pages.TestWishlist import wishlist
from Utilities import XLUtilities
from Utilities.Customelogger import loggings
from Utilities.readproprties import readconfig


class Test_001_logout:
    path = "/Users/sikalidas/PycharmProjects/FlipkartProject_Main/TestData/Userdetails.xlsx"

    URL = XLUtilities.readData(path, 'Sheet3', 2, 2)
    usernamee = XLUtilities.readData(path, 'Sheet2', 2, 1)
    Password = XLUtilities.readData(path, 'Sheet2', 2, 2)
    logeer = loggings.loggen()

    def test_Addproducts(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.key = loginpages(self.driver)
        self.key.setusername(self.usernamee)
        self.key.setpassword(self.Password)
        self.key.clicklogin()
        time.sleep(10)
        self.key2 = wishlist(self.driver)
        prf = self.key2.myprofile()
        veria = ActionChains(self.driver).move_to_element(prf)
        veria.perform()
        time.sleep(5)
        self.key1=logout(self.driver)
        self.key1.myprofile()
        time.sleep(5)
        global url
        url=self.driver.current_url
        print(url)
        self.key1.clicklogout()
        time.sleep(10)
        url1=self.driver.current_url
        print(url1)
        if url != url1:
            assert True
        else:
            self.driver.save_screenshot(".//Screenshort//" + "Test_001_logout.png")
            assert False