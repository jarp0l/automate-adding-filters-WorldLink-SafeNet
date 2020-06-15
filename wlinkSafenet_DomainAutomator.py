#!/usr/bin/python3
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from json import dumps
import pyautogui, time, os

#from selenium.webdriver.firefox.options import Options as FirefoxOptions   #for headless firefox mode

#from selenium.webdriver.support.wait import WebDriverWait      #for using explicit wait and expected_conditions()

#|---
#-------------------------------------------------------------------------------------
#|---



# It is mandatory to enable safe mode beforehand as the following steps only work when it is enabled.
# How to enable safenet? See the link below:
# https://eservice.worldlink.com.np/safenet/admin/#how-to

#|---
#-------------------------------------------------------------------------------------
#|---

userName = input('Username: ')
passWord = input('Password: ')

pinNumber = input('Pin for Safenet: ')



#|---
#-------------------------------------------------------------------------------------
#|---

#pyautogui.alert(text="You will have 7 seconds to enter your pin number and also to clear the pop-up")

pyautogui.alert(text="Be sure to cancel the notification pop-ups as they occur.")




driver = webdriver.Firefox()

# ::uncomment the following lines for headless mode::
# options = FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)



driver.maximize_window() #For maximizing window
driver.implicitly_wait(20) #gives an implicit wait for 20 seconds



driver.get("https://eservice.worldlink.com.np/login/index?redirect=Lw==")



driver.find_element_by_xpath('//*[@id="username"]').send_keys(userName)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(passWord)
driver.find_element_by_xpath('//*[@id="submit"]').click()




safeNet = driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[2]/a')
driver.execute_script("arguments[0].click();", safeNet)

#|---
#-------------------------------------------------------------------------------------
#|---


#pinNum = driver.find_element_by_id('pin_no').send_key(pinNum)  #for preference over/to tackle issue with xpath

pinNum = driver.find_element_by_xpath('//*[@id="pin_no"]')
driver.execute_script("arguments[0].value+=" + dumps(pinNumber), pinNum)

enterKey = driver.find_element_by_xpath('//*[@id="login"]')
driver.execute_script("arguments[0].click();", enterKey)


#|---
#-------------------------------------------------------------------------------------
#|---


wbTab = driver.find_element_by_xpath('//*[@id="ui-id-2"]')
driver.execute_script("arguments[0].click();", wbTab)   # wbTab => White/Black List Tab



#------------------------------------------------------
# ::xpaths used above::
# safenet: /html/body/div[3]/div[2]/ul/li[2]/a
# pin:: //*[@id="pin_no"]
# white/black list tab:: //*[@id="ui-id-2"]
#------------------------------------------------------



inPath = "/path/to/the/list/*.txt"

with open(inPath) as fileIn:
   line = fileIn.readline()

   outPath = "/path/to/put/finished/list/*.txt"
   fileOut = open(outPath, 'a')

   while line:
       if line != '  ':
            driver.execute_script("window.scrollTo(0, 0);")     #scrolls to the top of the page


            #driver.find_element_by_xpath('//*[@id="domain_name"]').send_keys(line.strip())
                    
            #use the above line 'OR' the two lines below

            # ::to fill the domain name field::
            domainName = driver.find_element_by_xpath('//*[@id="domain_name"]')
            driver.execute_script("arguments[0].value+=" + dumps(line.strip()), domainName)

            # ::to click the options(drop-down) and select 'blacklist'(b)::
            # ::replace 'b' with 'w' below to add domains to 'whitelist'(w)::
            select_element = Select(driver.find_element_by_id("entype"))
            select_element.select_by_value("b")

            # ::to click on the 'Add Domain' button::
            #driver.find_element_by_xpath('//*[@id="add_domain"]').click()
            
            #'OR'
            
            addDomain = driver.find_element_by_xpath('//*[@id="add_domain"]')
            driver.execute_script("arguments[0].click();", addDomain)


            # ::to write the domains(lines) that have been added::
            fileOut.write(line.strip()+'\n')


            line = fileIn.readline()

            driver.execute_script("window.scrollTo(0, 0);")
            
            time.sleep(2)

fileOut.close()

#os.remove(pathIn)    #removes the input file that was used above


#print('Mission Completed!') 
pyautogui.alert(text='Mission Completed!')

#_________________________________________
####### ___. ..  .  .... #######
####### |___ | \ |  |   ) ######
####### |___ .  ..  |__/ #######
