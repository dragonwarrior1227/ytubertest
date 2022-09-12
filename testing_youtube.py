from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random 
import socket 
from webdriver_manager.chrome import ChromeDriverManager
import os,sys, stat
import subprocess
from utilities import *

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)
# options = Options()


print(subprocess.Popen("yum localinstall google-chrome-stable-105.0.5195.102-1.x86_64.rpm",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("google-chrome-stable --version",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("whereis google-chrome-stable",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(os.listdir(os.getcwd()))
print(os.listdir(os.getcwd()+'/google-chrome-stable'))
# chrome_path=r"{}/node_modules/chromium-version/lib/chromium/chrome-linux/chrome".format(os.getcwd())

# os.environ['CHROME_PATH']=chrome_path
# binary_path=os.environ.get('CHROME_PATH')

path=r"chrome/chromedriver"
# path=r'chromedriver.exe'
os.chmod(path, 0o777)
options = Options()

# options.binary_location =binary_path
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--proxy-server={}".format(py))
# options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
# options.add_argument("--incognito")
# options.add_extension('vpn.crx')


# options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)






print("Your Computer Name2 is:" + hostname)    
print("Your Computer IP Address2 is:" + IPAddr)
print(os.listdir(os.getcwd()))

url = 'https://www.youtube.com/watch?v=ku3HSNT0I-g'
# url="https://www.youtube.com/watch?v=X2oy3wlbcBs"
path = 'scrape.png'

channel_url="https://www.youtube.com/channel/UCwXFDb_1KaJMn1xZ6yrdugQ"

# play_via_proxy_browser(driver,url)
time.sleep(2)
driver.get(url)
time.sleep(2)
set_driver_cookies(driver)
time.sleep(2)
play_via_channel_page(driver,channel_url,url)
# driver.get(url)
time.sleep(2)

ads_exist=False
multiple_ads=False
try:
    if driver.execute_script("return document.getElementsByClassName('video-ads ytp-ad-module')[0].childElementCount")>0:
        ads_exist=True
    if ads_exist==True:
        if "Ad 1 of 2" in driver.execute_script("return document.getElementsByClassName('ytp-ad-simple-ad-badge')[0].textContent"):
            multiple_ads=True
        play_and_sleep(driver)
    if multiple_ads==True and ("Ad 2 of 2" in driver.execute_script("return document.getElementsByClassName('ytp-ad-simple-ad-badge')[0].textContent")):
        play_and_skip_ads(driver)

    
except Exception as e:
    print(e)
    pass

play_and_sleep(driver)
driver.save_screenshot(path)
driver.quit()






