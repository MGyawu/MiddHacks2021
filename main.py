from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://vermont.force.com/events/s/search-events")
driver.implicitly_wait(2)

#Dictionary of xpath for all counties
countyDict = {}
countyDict["addison"] = '//*[@id="input-7-0-7"]'
countyDict["bennington"] = '//*[@id="input-7-1-7"]'
countyDict["caledonia"] = '//*[@id="input-7-2-7"]'
countyDict["chittenden"] = '//*[@id="input-7-3-7"]'
countyDict["essex"] = '//*[@id="input-7-4-7"]'
countyDict["franklin"] = '//*[@id="input-7-5-7"]'
countyDict["grand Isle"] = '//*[@id="input-7-6-7"]'
countyDict["lamoille"] = '//*[@id="input-7-7-7"]'
countyDict["orange"] = '//*[@id="input-7-8-7"]'
countyDict["orleans"] ='//*[@id="input-7-9-7"]'
countyDict["rutland"] = '//*[@id="input-7-10-7"]'
countyDict["washington"] = '//*[@id="input-7-11-7"]'
countyDict["windham"] = '//*[@id="input-7-12-7"]'
countyDict["windsor"] = '//*[@id="input-7-13-7"]'


#Select county based on user input
county = countyDict[input("Enter your county: ").lower()]
driver.find_element_by_xpath('//*[@id="input-7"]').click()
driver.find_element_by_xpath(county).click()

#Change Date Range?? Might not be necessary
driver.find_element_by_xpath('//*[@id="input-11"]').click()


#Need to hit search
