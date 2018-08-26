#coding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

def browser(address):
    driver = webdriver.Remote(command_executor='http://%s/wd/hub' % address,desired_capabilities=DesiredCapabilities.CHROME)
    print ("driver = webdriver.Remote(command_executor='%s',desired_capabilities=DesiredCapabilities.CHROME)" % address)
    return driver


#driver=browser("172.16.205.124:4454")
#driver.get("http://172.16.130.60:8100")
