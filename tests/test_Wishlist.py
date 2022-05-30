import time
from re import search

from selenium.webdriver import ActionChains

from Pages.Loginpage import loginpages
from Pages.TestCartFunctionality import cartfunctionality
from Pages.TestWishlist import wishlist
from Utilities import XLUtilities

from Utilities.Customelogger import loggings
from Utilities.readproprties import readconfig


class Test_001_Wishlist:
    path = "/Users/sikalidas/PycharmProjects/FlipkartProject_Main/TestData/Userdetails.xlsx"

    URL = XLUtilities.readData(path, 'Sheet3', 2, 2)
    usernamee = XLUtilities.readData(path, 'Sheet2', 2, 1)
    Password = XLUtilities.readData(path, 'Sheet2', 2, 2)
    logeer = loggings.loggen()
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
        self.key2=wishlist(self.driver)
        ref=self.key2.howeroverfasion()
        act=ActionChains(self.driver).move_to_element(ref)
        act.perform()
        #   inspect the element which is hidden  "command+\"
        self.key2.menstopwear(1)
        self.key2.subsection(1)
        self.key1=cartfunctionality(self.driver)
        time.sleep(20)
        self.key1.selectfirstprod(2)
        str = self.driver.window_handles[1]
        self.driver.switch_to.window(str)
        time.sleep(20)
        text1=self.key2.storeprdtext()
        my_list.append(text1.text)
        self.key2.addtowishlist()
        self.key2.clickhomepage()
        time.sleep(10)
#     second product to wishlist
        ref2 = self.key2.howeroverfasion()
        act = ActionChains(self.driver).move_to_element(ref2)
        act.perform()
        ref3=self.key2.womenethenic()
        act1=ActionChains(self.driver).move_to_element(ref3)
        act1.perform()
        self.key2.subsection(2)
        time.sleep(20)
        self.key2.addfirstsare()
        time.sleep(20)
        str1 = self.driver.window_handles[2]
        self.driver.switch_to.window(str1)
        time.sleep(20)
        text2=self.key2.storeprdtext()
        my_list.append(text2.text)
        self.key2.addtowishlist()
        prf=self.key2.myprofile()
        veria=ActionChains(self.driver).move_to_element(prf)
        veria.perform()
        time.sleep(5)
        self.key2.clickonwishlist()
        time.sleep(10)
        item=self.key2.wishlistitems()
        for itm in item:
            my_list1.append(itm.text)
        count=0
        for i in my_list:
            for j in my_list1:
                if i.find(j):
                    count=1
        if count ==1:
            assert True
        else:
            self.driver.save_screenshot(".//Screenshort//" + "Test_001_Wishlist.png")
            assert False