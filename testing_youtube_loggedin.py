from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random 
import os,sys, stat
import subprocess
from xvfbwrapper import Xvfb
from utilities import *


print(subprocess.Popen("yum localinstall google-chrome-stable.rpm",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("yum -y install xorg-x11-server-Xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
vdisplay = Xvfb()
vdisplay.start()
chrome_path=r"/usr/bin/google-chrome-stable"
os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')
path=r"chrome/chromedriver"
# path=r"chrome/chromedriver.exe"
os.chmod(path, 0o777)
options = Options()
options.binary_location =binary_path
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")
user_agent= get_user_agent()
if user_agent is not None:
    options.add_argument('--user-agent='+user_agent)





try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)



driver.get("https://www.youtube.com")
time.sleep(3)


try:

    c3_eles= driver.execute_script("return document.getElementsByClassName('c3-material-button-button')")
    print("c3 eles",len(c3_eles))
    if len(c3_eles)>0:
        for i in range(0,len(c3_eles)):
            if 'Accept' in driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].textContent"):
                time.sleep(5)
                driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].click()")
                print("c3 click")
            else:
                print("c3 change",driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].textContent"))
    else:
        print("No c3 buttons")
except Exception as e:
    print("c3 error",e)
    pass



video_url,channel_url=get_random_video()

driver.get("https://www.youtube.com")
time.sleep(2)


set_driver_cookies(driver)
driver.refresh()

play_types = [play_via_channel_page,play_via_youtube_search,direct_play]
fun = random.choice(play_types) # This picks one function from sums list
fun(driver,video_url,channel_url) # This calls the picked function
time.sleep(2)


try:
    time.sleep(2)
    c3_eles= driver.execute_script("return document.getElementsByClassName('c3-material-button-button')")
    if len(c3_eles)>0:
        for i in range(0,len(c3_eles)):
            if 'Got it' in driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].textContent"):
                time.sleep(5)
                driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].click()")
                print("c3 click")
except Exception as e:
    print("c3 error",e)
    pass


# driver.save_screenshot("final_shot.png")
# upload_basic("final_shot.png")




ads_exist=False
multiple_ads=False
ads_func_list=[play_and_sleep,play_and_skip_ads]
adfunc=None
try:
    if driver.execute_script("return document.getElementsByClassName('video-ads ytp-ad-module')[0].childElementCount")>0:
        ads_exist=True
        print("Ad exist")
    if ads_exist==True:
        if "Ad 1 of 2" in driver.execute_script("return document.getElementsByClassName('ytp-ad-simple-ad-badge')[0].textContent"):
            multiple_ads=True
            print("multiple ads exist")
        adfunc=random.choice(ads_func_list)
        adfunc(driver)
    if multiple_ads==True and adfunc==play_and_sleep and ("Ad 2 of 2" in driver.execute_script("return document.getElementsByClassName('ytp-ad-simple-ad-badge')[0].textContent")):
        print("Entering Ad2")
        adfunc=random.choice(ads_func_list)
        adfunc(driver)

    
except Exception as e:
    print("main Exception on ads", e)
    pass

print("start playing")
play_and_sleep(driver)


driver.quit()







vdisplay.stop()