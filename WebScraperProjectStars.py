#Step 1: Importing Files

#Used to parse
import selenium
from selenium import webdriver
browser = webdriver.Edge()
from bs4 import BeautifulSoup
#Used to make the code sleep
import time
#Used for csv extensions
import csv

#Step 2: The Link

#Creating The Link
start_url = "https://en.wikipedia.org/wiki/Lists_of_stars"
#Setting Up The Link With Chrome
browser = webdriver.Edge("C:/Users/Jayan/WebScraper/msedgedriver.exe")
#Getting The Link Ready With Chrome
browser.get(start_url)

#Step 3: Info

#Creating A Function To Get Info
def Scrape():
    #Setting Header Names
    Headers = ["Name", "Light Years From Earth", "Mass", "Stellar Magnitude", "Discovery Date"]
    #Setting Planet Data To Nothing
    Planet_Data = []
    #Opening The Browser Using BeautifulSoup And Then Parsing
    Soup = BeautifulSoup(browser.page_source, "html.parser")
    #Finding All The Tags With Class And Exoplanet
    for UL_Tag in Soup.find_all("UL", attrs = {"class", "exoplanet"}):
        #Setting LI_Tags
        LI_Tags = UL_Tag.find_all("LI")
        #Setting temp_list To An Empty List
        temp_list = []
    #Checking HTML With EdgeDriver
        for Index, LI_Tags in enumerate(LI_Tags):
            #Sorting Names Into Alphabetical Order
            if Index == 0:
                temp_list.append(LI_Tags.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(LI_Tags.contents[0])
                except:
                    temp_list.append("")

#Final Step: Calling The Function

Scrape()