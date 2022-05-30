import time

from Pages.Loginpage import loginpages
from Pages.TestCartFunctionality import cartfunctionality
from Utilities import XLUtilities
from Utilities.Customelogger import loggings
from Utilities.Datadriven import data
from Utilities.readproprties import readconfig


class Test_001_cartfunction:
    path = "/Users/sikalidas/PycharmProjects/FlipkartProject_Main/TestData/Userdetails.xlsx"
    URL = XLUtilities.readData(path, 'Sheet3', 2, 2)
    usernamee = XLUtilities.readData(path, 'Sheet2', 2, 1)
    Password = XLUtilities.readData(path, 'Sheet2', 2, 2)
    logeer = loggings.loggen()
    prod=XLUtilities.readData(path, 'Sheet4', 2, 2)
    prod1=XLUtilities.readData(path, 'Sheet4', 3, 2)
    prod2=XLUtilities.readData(path, 'Sheet4', 4, 2)
    pin=XLUtilities.readData(path, 'Sheet1', 3, 2)
    global my_list
    my_list = []
    global my_list1
    my_list1 =[]

    def test_Addproducts(self,setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.key = loginpages(self.driver)
        self.key.setusername(self.usernamee)
        self.key.setpassword(self.Password)
        self.key.clicklogin()
        time.sleep(10)
        self.key1=cartfunctionality(self.driver)
        self.key1.searchproduct(self.prod)
        time.sleep(10)
        # special feature where code is optimized
        self.key1.selectfirstprod(1)
        time.sleep(10)
        p = self.driver.current_window_handle
        size=self.driver.window_handles
        for i in size:
            if (i != p):
                self.driver.switch_to.window(i)
                break
        veri=self.driver.title
        # store the object name
        time.sleep(5)
        global product1
        product1 = self.key1.storethevalue()
        my_list.append(product1)
        # if veri== data.producttile:
        #     assert True
        # else:
        #     assert False
        # Add pincode
        # self.key1.addpincode(self.pin)
        time.sleep(10)
        self.key1.addtocart()
        time.sleep(10)
        self.key1.searchproduct(self.prod1)
        time.sleep(20)
        veri1=self.driver.title
        # if veri1==data.shirt:
        #     assert True
        # else:
        #     assert False
        # special feature
        self.key1.selectfirstprod(2)
        str=self.driver.window_handles[2]
        self.driver.switch_to.window(str)
        time.sleep(30)
        # store the object name
        global product2
        product2 = self.key1.storethevalueforshirt()
        my_list.append(product2)
        self.key1.selectsihirtsize()
        time.sleep(40)
        self.key1.addtocart()
        time.sleep(10)
        self.key1.searchproduct(self.prod2)
        time.sleep(20)
        ver2=self.driver.title
        # if ver2== data.Washingmaching:
        #     assert True
        # else:
        #     assert False
        # special feature
        self.key1.selectfirstprod(3)
        str1=self.driver.window_handles[3]
        self.driver.switch_to.window(str1)
        time.sleep(20)
        # store the object name
        global product3
        product3 = self.key1.storevalueforwashing()
        my_list.append(product3)
        self.key1.addtocart()
        time.sleep(10)
        # pending to verify
        print(my_list)
        iteams=self.key1.checkthecart()
        for item in iteams:
           my_list1.append(item.text)
        print(my_list1)
        count=0
        for item in my_list:
            for item1 in my_list1:
                if item.find(item1):
                    count=1
        if count == 1:
            assert True
        else:
            self.driver.save_screenshot(".//Screenshort//" + "Test_001_cartfunction.png")
            assert False