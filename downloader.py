from six.moves.urllib.request import urlretrieve

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

    locationString = 'chromedriver.exe'

driver = webdriver.Chrome(executable_path=(locationString))
driver.set_window_position(4000, 651)
driver.set_page_load_timeout(600)
