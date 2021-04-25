from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import numpy as np
import time
from datetime import datetime
import tkinter as tk

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()

# This makes it run in the background
options.add_argument("headless")
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://vermont.force.com/events/s/search-events")
driver.implicitly_wait(2)


#NEED THESE IF NOT USING GUI
county = input("Enter your county: ")
curAppt = input("Enter the date of your current appointment (mm/dd/yy): ")
curAppt = datetime.strptime(curAppt, '%m/%d/%y')

# Dictionary of xpath for all counties
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
countyDict["orleans"] = '//*[@id="input-7-9-7"]'
countyDict["rutland"] = '//*[@id="input-7-10-7"]'
countyDict["washington"] = '//*[@id="input-7-11-7"]'
countyDict["windham"] = '//*[@id="input-7-12-7"]'
countyDict["windsor"] = '//*[@id="input-7-13-7"]'

#WITHOUT THE GUI
def main(county, curAppt):


#THIS IS WITH THE GUI
#def main(county,appt):
    # Select county based on user input
    #curAppt = datetime.strptime(dateVar.get(), '%m/%d/%y')
    #countyX = countyDict[(countyVar.get()).lower()]

    #curAppt = datetime.strptime(appt, '%m/%d/%y')
    countyX = countyDict[(county.lower())]

    #curAppt = datetime.strptime(curAppt, '%m/%d/%y')
    #countyX = countyDict[county.lower()]
    driver.find_element_by_xpath('//*[@id="input-7"]').click()
    driver.find_element_by_xpath(countyX).click()

    # Change Date Range to next 7 days
    #driver.find_element_by_xpath('//*[@id="input-11"]').click()
    #driver.find_element_by_xpath('//*[@id="input-11-3-11"]').click()

    # Need to hit search
    driver.find_element_by_xpath(
        '//*[@id="main-content"]/div/div[2]/div/div/c-vtts_cp_search-event-public/div/div/c-vtpc-site-map/div/lightning-layout/slot/c-vt_event_scheduler_filters/div[2]/div/lightning-button[1]/button').click()

    appt = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div[2]/div/div/c-vtts_cp_search-event-public/div/div/c-vtpc-site-map/div/div/div/lightning-layout/slot/lightning-layout-item[2]/slot/div/c-okpc-event-list-item[*]/div/lightning-layout/slot/lightning-layout-item[*]')

    i = 0
    apptArray = np.empty((len(appt) // 3, 3), dtype=object)
    while i <= len(appt) - 3:
        apptArray[i // 3] = ([appt[i].text, appt[i + 1].text, appt[i + 2].text])
        # print("Entry 1: " + appt[i].text,"Entry 2: "  + appt[i+1].text,"Entry 3: " + appt[i+2].text)
        i += 3

    formattedDates = []
    i = 0
    while i <= len(appt) - 3:
        rawDate = appt[i].text
        formDate = ''
        if 'Jan' in rawDate:
            formDate += '01/'
        elif 'Feb' in rawDate:
            formDate += '02/'
        elif 'Mar' in rawDate:
            formDate += '03/'
        elif 'Apr' in rawDate:
            formDate += '04/'
        elif 'May' in rawDate:
            formDate += '05/'
        elif 'Jun' in rawDate:
            formDate += '06'
        elif 'Jul' in rawDate:
            formDate += '07'
        elif 'Aug' in rawDate:
            formDate += '08'
        elif 'Sep' in rawDate:
            formDate += '09'
        elif 'Oct' in rawDate:
            formDate += '10'
        elif 'Nov' in rawDate:
            formDate += '11'
        elif 'Dec' in rawDate:
            formDate += '12'

        if rawDate[5] == ',':
            formDate += '0' + rawDate[4] + '/21'
        else:
            formDate += rawDate[4] + rawDate[5] + '/21'
        formattedDates.append(formDate)
        i += 3
    # print(formattedDates)
    apptArrayRef = []

    for date in formattedDates:
        apptArrayRef.append(datetime.strptime(date, '%m/%d/%y'))

    earlierAppt = np.empty((len(appt) // 3, 3), dtype=object)
    i = 0
    for elem in apptArrayRef:
        if elem < curAppt:
            earlierAppt[i] = apptArray[i]
            i += 1

    # Neaten up the return

    cleanElements = []
    for elem in earlierAppt:
        if elem[0] != None:
            cleanElements.append(elem[1])
    if len(cleanElements) == 0:
        output = "There aren't currently any earlier appointments available. We'll keep checking!"
        print(output)
        #return output
        return 0
    else:
        output = "There are " + str(len(cleanElements)) + " earlier appointments available.\n They are: \n"
        #print("There are " + str(len(cleanElements)) + " earlier appointments available.")
        #print("They are: ")
        label = 0
        for elem in cleanElements:
            output += str(label) +": " + elem + '\n'
            label += 1
        print(output)
        #return output

    chosenDate = int(input("Which date would you like to see? (#)"))
    chosenDate *= 3


    driver.execute_script("arguments[0].click();",appt[chosenDate])

    next = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/div/c-vtts_cp_search-event-public/div/footer/lightning-button/button')
    driver.execute_script("arguments[0].click();", next)

    #//*[@id="main-content"]/div/div[2]/div/div/c-vtts_cp_search-event-public/div/div/c-vtts_cp_calendar/div[2]/table/tbody/tr[1]
    times = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/div/c-vtts_cp_search-event-public/div/div/c-vtts_cp_calendar/div[2]/table/tbody/tr[*]')

    for element in times:
        if (element.text.find("Not") == -1):
            print(element.text)
    print("To book your appointment, create an account or login at https://vermont.force.com/events/s/selfregistration")
    return 1


#Runs the program repeatedly until earlier appointments are found
retVal = 0
while retVal == 0:
    retVal = main(county,curAppt)
    time.sleep(5)



"""
#GUI


top = tk.Tk()

countyVar=tk.StringVar()
dateVar=tk.StringVar()

countyLabel = tk.Label(top, text='County', font=('calibre', 10, 'bold'))
countyEntry = tk.Entry(top, textvariable=countyVar, font=('calibre', 10, 'normal'))

dateLabel = tk.Label(top, text='Current Appointment', font=('calibre', 10, 'bold'))
dateEntry = tk.Entry(top, textvariable=dateVar, font=('calibre', 10, 'normal'))

result = tk.Label(top, text='')
result.grid(row=2, column=0, columnspan=2)

sub_btn=tk.Button(top, text = 'Submit')
sub_btn.config(command=lambda: result.config(text=main(countyVar.get(),dateVar.get())))

countyLabel.grid(row=0,column=0)
countyEntry.grid(row=0,column=1)
dateLabel.grid(row=1,column=0)
dateEntry.grid(row=1,column=1)
sub_btn.grid(row=0,column=5)


top.mainloop()
"""
