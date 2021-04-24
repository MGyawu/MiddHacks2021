# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://vermont.force.com/events/s/search-events/")

try:
    elem = driver.find_element_by_xpath("//*[@id='input-7']")
    # elem.click()
    select = Select(elem)
    select.select_by_visible_text('Addison')
except NoSuchElementException:
    pass
# username = driver.find_elements_by_name("username")
# password = driver.find_elements_by_name("password")
# print(type(username))
# username.send_keys("tyou@middlebury.edu")
# username.sendkeys(Keys.RETURN)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
