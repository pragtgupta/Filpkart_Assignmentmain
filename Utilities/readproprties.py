import configparser

import Configuration
from Utilities import XLUtilities

config=configparser.RawConfigParser()
config.read(".//Configuration//config.ini")


class readconfig():

    @staticmethod
    def getapplicationurl():
        URL=config.get('Common info','URL')
        return URL

    @staticmethod
    def getusername():
        username = config.get('Common info', 'usernamee')
        return username

    @staticmethod
    def getpassword():
        password = config.get('Common info', 'Password')
        return password
    @staticmethod
    def products():
        product=config.get('Common info', 'product')
        return product
    @staticmethod
    def products1():
        product1=config.get('Common info', 'product1')
        return product1
    @staticmethod
    def products2():
        products2=config.get('Common info', 'product2')
        return  products2
    @staticmethod
    def addpincode():
        pincode=config.get('Common info', 'pincode')
        return pincode

# search and filter

    @staticmethod
    def searchproduct():
        producttosearched=config.get('Common info', 'producttobesearch')
        return producttosearched
    @staticmethod
    def brand():
        brandtosearch=config.get('Common info', 'brand')
        return brandtosearch


