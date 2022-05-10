import undetected_chromedriver.v2 as uc
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests, random
from bs4 import BeautifulSoup
import csv 
import os

def loginlink(searchterm):
    wordlist = []
    multiplesearchterms = ''
    numwords = searchterm.split()
    if len(numwords) == 1:
        link = "https://www.pexels.com/search/{}".format(searchterm)
        return link
    else:
        for words in numwords:
            template = "%20"
            newsearchword = words+template
            wordlist.append(newsearchword)
        for terms in wordlist:
            multiplesearchterms+=terms
        link = "https://www.pexels.com/search/{}".format(multiplesearchterms)
        return link
listlinks = []
linkList = []
searchterm = input("Enter what you want to search.....:")
turns = int(input("Number of Turns: "))
chrome = 'chromedriver.exe'
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user_agent=DN")
chrome_options.headless = True
driver = uc.Chrome(options=chrome_options)
driver.delete_all_cookies()
time.sleep(2)
actions = ActionChains(driver)
loginlink = loginlink(searchterm)
time.sleep(2)
driver.get(loginlink)
print("Waiting for links to load.........")
time.sleep(5)
for n in range(0,turns):
    time.sleep(0.32)
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
lnks=driver.find_elements_by_tag_name("a")
for lnk in lnks:
    k = (lnk.get_attribute("href"))
    listlinks.append(k)
print("{} Links Retrieved".format(len(listlinks)))
count = 0
newpath = 'C:/Users/Kshitij/Notebooks/Pexel Image Downloader/Images/{}'.format(searchterm) 
if not os.path.exists(newpath):
    os.makedirs(newpath)
else:
    print("Folder Available")
    exit()
print("{} Folder Created".format(searchterm))
sett = set(listlinks)
for p in sett:
    if "jpeg" in p or "jpg" in p:
        linkList.append(p)
    else:
        continue
print("{} Images will be downloaded....".format(len(linkList)))       
for links in linkList:
        try:
            randomno = random.randint(1,10000)
            f= open("C:/Users/Kshitij/Notebooks/Pexel Image Downloader/Images/"+str(searchterm)+'/'+str(randomno)+'.jpg','wb')
            f.write(requests.get(links).content)
            f.close()
            count +=1
        except:
            print("No Image found")
print("Downloaded {} Images....".format(count))
driver.close()