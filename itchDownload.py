from bs4 import BeautifulSoup
from selenium import webdriver
from six.moves.urllib.request import urlretrieve
import glob
import os
import re
import sys
import time
import zipfile

dragNDrop = ''.join(sys.argv[1:])
done = False
owd = os.getcwd()
if not os.path.exists(os.environ['temp'] + "\itchiotempdir"):
    os.makedirs(os.environ['temp'] + "\itchiotempdir")
downloadDir = os.environ['temp'] + "\itchiotempdir"

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : downloadDir}
chromeOptions.add_experimental_option("prefs",prefs)

if os.path.isfile('chrome.ini'):
    ini = open('chrome.ini', 'r')
    locationString = ini.read()
elif os.path.isfile('chromedriver.exe'):
    locationString = 'chromedriver.exe'
else:
    response = urlretrieve('https://chromedriver.storage.googleapis.com/2.33/chromedriver_win32.zip','chromedriver.zip')

    zip_ref = zipfile.ZipFile("chromedriver.zip", 'r')
    zip_ref.extractall(owd)
    zip_ref.close

    os.remove("chromedriver.zip")

    locationString = 'chromedriver.exe'

driver = webdriver.Chrome(executable_path=(locationString), chrome_options=chromeOptions)
driver.set_window_position(4000, 651)
driver.set_page_load_timeout(600)

if os.path.isfile("repo.ini"):
    with open ("repo.ini", "r") as myfile:
        fullURL = myfile.read()
        doubSlash = fullURL.index("//")
        ioSlash = fullURL.index("io/")
        gameName = fullURL[ioSlash+3:]
        teamName = fullURL[doubSlash+2:ioSlash-6]
elif dragNDrop == "":
    teamName = raw_input("\nInput the Team Name\n>")
    gameName = raw_input("\nInput the Game Name\n>")
else:
    doubSlash = dragNDrop.index("//")
    ioSlash = dragNDrop.index("io/")
    gameName = dragNDrop[ioSlash:]
    teamName = dragNDrop[doubSlash:ioSlash-6]

siteString = "https://" + teamName + ".itch.io/" + gameName

driver.get(siteString)

driver.find_element_by_xpath("//a[@class='button buy_btn']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='direct_download_btn']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='button download_btn']").click()

while done == False:
    for fname in os.listdir(downloadDir):
        if fname.endswith('.zip'):
            done = True

os.chdir(downloadDir)
for file in glob.glob("*.zip"):
    zipFile = file

zip_ref = zipfile.ZipFile(zipFile, 'r')
zip_ref.extractall(owd)
zip_ref.close

time.sleep(2)

driver.close()
