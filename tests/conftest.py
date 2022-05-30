import pytest
from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'/Users/sikalidas/PycharmProjects/Mini_Assignment_CheckTemp/Drivers/chromedriver')
    return driver

@pytest.fixture()
def setup1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'/Users/sikalidas/PycharmProjects/Mini_Assignment_CheckTemp/Drivers/chromedriver')
    return driver

# Pytest Html report

def pytest_configure(config):
    config._metadata['Project Name'] ='Flipkart'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Siddharth'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
