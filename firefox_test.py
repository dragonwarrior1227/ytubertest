from selenium import webdriver
import time
import os,sys, stat
import subprocess
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

from webdriver_manager.firefox import GeckoDriverManager


try:
    # Fire a remote Firefox instance using geckodriver.
    # You need to have Geckodriver in the same directory as the automation testing script OR
    # you need to add it in the "path" environment variable OR 
    # you need to know the full path to the geckodriver executable file and use it as:
    # binary = FirefoxBinary('')
    # print(os.environ.get('PATH'))

    print(subprocess.Popen("yum localinstall opera.rpm",shell=True,stdout=subprocess.PIPE).communicate()[0])
    print(subprocess.Popen("opera --version",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen("/vercel/path0/browser/firefox/firefox --version",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen("stat /vercel/path0/browser/firefox/firefox",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen("cd ./browser/firefox & ls ",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen("cd browser/firefox & stat firefox ",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # # print(subprocess.Popen(" yum localinstall firefox.rpm --skip-broken",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen("yum install wget",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen("""wget -O- "https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US" | tar -jx -C /usr/local/""",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen("mv /usr/bin/firefox /usr/bin/backup_firefox",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen("""echo "exclude=firefox" >> /etc/dnf/dnf.conf""",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen("""ln -s /usr/local/firefox/firefox /usr/bin/firefox""",shell=True,stdout=subprocess.PIPE).communicate()[0])
    # print(subprocess.Popen(os.getcwd()+"/browser/firefox/firefox --help",shell=True,stdout=subprocess.PIPE).communicate()[0])
    options = Options()
    print(os.listdir(os.getcwd()+'/browser/firefox'))
    # print(os.listdir(os.getcwd()+'/browser/firefox/firefox-bin'))
    options.binary_location ='/vercel/path0/browser/firefox/firefox'
    options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)


 
    # driver = webdriver.Firefox()
 
    # path to your downloaded Firefox addon extension XPI file
 
    extension_path = r"chrome/urban_vpn.xpi"
 
    # using webdriver's install_addon API to install the downloaded Firefox extension
 
    driver.install_addon(extension_path, temporary=True)
 
    # Opening the Firefox support page to verify that addon is installed
 
    driver.get("about:support")
 
    # xpath to the section on the support page that lists installed extension
 
    addons = driver.find_element("xpath",'//*[contains(text(),"Add-ons") and not(contains(text(),"with"))]')

    # scrolling to the section on the support page that lists installed extension
 
    driver.execute_script("arguments[0].scrollIntoView();", addons)
 
    # introducing program halt time to view things, ideally remove this when performing test automation in the cloud using LambdaTest
    driver.get("moz-extension://1910391e-18d1-4e55-a930-4e6168daf82d/popup/index.html#/main")
 
    print("Success. Yayy!!")
 
    time.sleep(20)
 
except Exception as E:
 
    print(E)
 
finally:
 
    # exiting the fired Mozilla Firefox selenium webdriver instance
 
    driver.quit()
 
    # End Of Script