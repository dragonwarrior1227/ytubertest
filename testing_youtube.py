from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random 
import os,sys, stat
import subprocess
# from pyvirtualdisplay import Display
from xvfbwrapper import Xvfb
from utilities import *


print(subprocess.Popen("yum localinstall google-chrome-stable.rpm",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("yum -y install xorg-x11-server-Xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("xvfb-run ",shell=True,stdout=subprocess.PIPE).communicate()[0])

vdisplay = Xvfb()
vdisplay.start()
# print(subprocess.Popen("google-chrome-stable --no-sandbox --load-extension= browser/eppiocemhmnlbhjplcgkofciiegomcon",shell=True,stdout=subprocess.PIPE).communicate()[0]) 
# print(subprocess.Popen("chrome/chromedriver.exe --load-and-launch-app = chrome/eppiocemhmnlbhjplcgkofciiegomcon",shell=True,stdout=subprocess.PIPE).communicate()[0])   
chrome_path=r"/usr/bin/google-chrome-stable"

os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')
path=r"chrome/chromedriver"
# path=r"chrome/chromedriver.exe"
os.chmod(path, 0o777)

options = Options()
# options.binary_location =binary_path
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


options.add_argument("--disable-gpu")
# options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
# options.add_argument("--incognito")
options.add_extension('chrome/vpn.crx')



try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)





driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html")
time.sleep(3)
# driver.save_screenshot("bits2.png")
# upload_basic("bits2.png")
print(driver.window_handles)
if len(driver.window_handles)>1:
    driver.switch_to.window(window_name=driver.window_handles[1])
    driver.close()
driver.switch_to.window(window_name=driver.window_handles[0])
time.sleep(3)


btn=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/button[2]").click()
time.sleep(1)
btn=driver.execute_script("return document.getElementsByClassName('select_location__button-box')[0].children[1].click()")
vpn_count=driver.execute_script("return document.getElementsByClassName('locations')[0].childElementCount")

random_vpn=random.randint(1,vpn_count)
print(vpn_count,random_vpn)
driver.execute_script("return document.getElementsByClassName('locations')[0].children[{}].click()".format(random_vpn))
time.sleep(2)
driver.save_screenshot("bits.png")
upload_basic("bits.png")



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







vdisplay.stop()