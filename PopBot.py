# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:46:35 2019
@author: Mercteria
"""

from selenium import webdriver
import datetime
import random
import os
import time
import sys

ismac = 0
log = ""

#conepat = os.getcwd()
conepat = os.path.dirname(os.path.abspath(__file__))
logfile = os.path.join(conepat,"log.txt")    
def logwrit(wbuff, path = logfile, mac = ismac):
    global log
    if ismac:
        log+=wbuff
    else:
        f= open(path,"a")
        f.write(wbuff+"\n")
        f.close()
    
def testlog():
    driverp = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "chromedriver.exe")
    print(driverp)
    logwrit("Local Driver Loading...")
    #Options for No GUI
    chrome_options = webdriver.ChromeOptions() 
    
    #use chrome webdriver
    browser = webdriver.Chrome(driverp,options=chrome_options)
    #open page
    browser.get('https://popcat.click/')
    for i in range(10):
        print(i+1)
        time.sleep(1)
    tapcnt = 0
    try:
        while True:
            slp = random.randint(0, 100)
            if slp > 10:
                print(tapcnt)
                element = browser.find_element_by_id('app').click()
                tapcnt+=1
                time.sleep(0.1)
            else:
                print("Sleep",str(slp),"sec")
                for t in range(slp):
                    print(t)
                    time.sleep(1)
                print("Continue")
        #browser.close()
    except KeyboardInterrupt:
        pass
    return tapcnt

taps = testlog()
logwrit("## Program END:"+str(datetime.datetime.now())+"\nTotal taps: "+str(taps))
    
