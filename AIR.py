# IT WORKS
# https://imgbb.com/
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from twilio.rest import Client

#import sys
#sys.path.insert(0, 'twilio')
# from variables import *

import xlwt
import sys
import csv
import math
from mortgage import Loan
import decimal
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
import plotly.express as px
import statistics
#from openpyxl import load_workbook
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0, '/Users/yu.liu@ibm.com/Documents/Atom/Python/Selenium/pandas/Functions')
from getDigitfromString import getDigitfromString
from not_available import not_available

# ######### CHANGE HERE!########################
# basic info
# ######### END CHANGE HERE!###############
# pages = list(range(1, page_input))
city_name = (input("What is the city you want to look at the air quality for? (Format: City, State): ") or "San Jose, CA")
url = ("https://www.airnow.gov")
#url = "https://www.zillow.com/homedetails/1201-Burnham-Dr-San-Jose-CA-95132/19773843_zpid/"
# Open the browser and URL
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()
time.sleep(2)

# item_list = driver.find_element_by_xpath("//span[@class='s-item__price']/span[contains(text(),'$')]")
# item_list = driver.find_element_by_xpath("//div[@class='s-item__image-wrapper']")


#print("item listed:" + str(item_list))
# Create the arrays to hold the values
price = []
date = []
name = []
ship = []
total = []

try:
    #income_x = (driver.find_element_by_xpath('(//div[@class="Spacer-sc-17suqs2-0 pfWXf"])[2]/p').text)
    # price_x = (driver.find_element_by_xpath('//span[contains(text(),"Rent Zestimate")]/following::p[1]').text)
    search_bar = driver.find_element_by_xpath("//input[@id='location-input_input']")
    search_bar.submit()
    search_bar.clear()
    search_bar.send_keys(city_name)  # **
    search_bar.submit()
    time.sleep(2)
    # price_x = float(price_x.replace('$', ''))

    # price_x = getDigitfromString(price_x)
    # print("PRICEX = " + price_x)
except:
    print("error")
    price.append("Not Available")
else:
    print("City found")
    price.append(search_bar)

# #print(income[house_cards[house]])
#
# # EXPENSES
#                                         #sc-Rmtcm GNsVX  sc-Rmtcm fzcNkq         Text-aiai24-0 cJeryq                        Text-aiai24-0 cJeryq
try:                                                         #sc-Rmtcm GNs
    #aqi = (driver.find_element_by_xpath('.//div[@class="aqi"]/b[1]').text)
    aqi = (driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/b[1]').text)
    print("AQI is: " + aqi)

except:
    date.append("N/A")
    print("MESSED UP")
else:
    date.append(aqi)
    print("AQI is: " + aqi)
    #print("AQI is: " + aqi2)
    #print(date_x)

# get link
link = driver.current_url
nearby = driver.find_element_by_xpath("//a[@id='air-quality-monitors-near-me']").get_attribute("href")
time.sleep(2)
# nearby = driver.current_url

aqi = int(aqi)

if aqi <= 50:
    status = "Good"
    message = "Go enjoy the fresh air"
elif aqi >= 50 and aqi <= 100:
    status = "Moderate"
    message = "Air Quality is not the best, shorten the amount of time outdoors"
elif aqi >= 100 and aqi <= 150:
    status = "Unhealthy for sensitive groups"
    message = "If you are sensitive, stay indoors. Wear a mask when out"
else:
    status = "Unhealthy"
    message = "Turn on your air purifier and stay indoors, wear masks if needed"

if city_name == "San Jose, CA":
    pic = 'https://i.ibb.co/nCGNfsN/SJ-AQI.png'
else:
    pic = 'https://i.ibb.co/wsn6s2F/LA-AQI.png'


print("The air quality status is: " + status)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = ACC_SID
auth_token = AUTH_TOK
client = Client(account_sid, auth_token)

myNumber = "+18056182885"
toNumber = '+12345567890'

print(nearby)

message = client.messages \
                .create(
                     body=("The air quality index today in " + city_name + " is "+ str(aqi) + " which is " + str(status) +". " + message + ". Get more information through: " + link + "\n And check nearby areas: " + nearby) ,
                     media_url=[pic],
                     from_=myNumber,
                     to=toNumber
                 )

print(message.sid)

# Close Listing
time.sleep(1)
