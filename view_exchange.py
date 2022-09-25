from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random 
import os,sys, stat,json
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
options.add_argument("--start-maximized");
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")
# user_agent= get_user_agent()
# if user_agent is not None:
#     options.add_argument('--user-agent='+user_agent)





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



# video_url,channel_url=get_random_video()

driver.get("https://www.youtube.com")
time.sleep(3)


# print(json.dumps(driver.get_cookies()))
set_driver_cookies(driver)
driver.refresh()

time.sleep(5)


driver.get("https://app.growviews.com/")
time.sleep(2)

# set_view_bot_cookies(driver)
# driver.refresh()
# time.sleep(2)

print("loading")
try:	
	driver.execute_script("return document.getElementById('adroll_allow_all').click()")
	ele=driver.execute_script("return document.forms[0].children[0].children[0]")
	ele.send_keys('vinay2210978@gmail.com')
	ele=driver.execute_script("return document.forms[0].children[1].children[0]")
	ele.send_keys('Musha22@')
	time.sleep(2)
	driver.execute_script("return document.forms[0].children[2].children[0].children[0].click()")
	time.sleep(3)
	driver.get("https://app.growviews.com/")
	time.sleep(2)
	print("clicking run")
	btns=driver.execute_script("return document.getElementsByTagName('button')")
	print("cliked run")
	if len(btns)>0:
		for i in range(0,len(btns)):
			if 'RUN' in driver.execute_script("return document.getElementsByTagName('button')["+str(i)+"].textContent"):
				driver.execute_script("return document.getElementsByTagName('button')["+str(i)+"].click()")
	else:
		print('no buttons')
except:
	print("run button error")

time.sleep(15)
driver.save_screenshot("final.png")
upload_basic("final.png")

print("started watchong")
time.sleep(1500)

driver.quit()


vdisplay.stop()