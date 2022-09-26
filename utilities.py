from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,random,os,json

import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import pandas as pd

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive',]
os.environ['SHEET_ID']='1hNx5JNmeYTmUSMp4Ke0qHaHaGqI4TtBJ63EuWfh3eAI'
sheet_id=os.environ.get('SHEET_ID')

def read_sheet(sheet_name="Sheet1"):
	url = "https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}".format(sheet_id,sheet_name)

	df=pd.read_csv(url)
	df=df.dropna(axis=1)
	print(df.head())
	return df

def upload_basic(img,fileid='1vheNuYHeH-BbmkuhRham7JhwphB4CFze'):
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {'name': img,'parents': ['1BbfqfiKbAcgPGpNv0Au4tZsmiUmCxe0H']}
        media = MediaFileUpload(img,
                                mimetype='image/png')
        # pylint: disable=maybe-no-member
        # file = service.files().create(body=file_metadata, media_body=media,
        #                               fields='id').execute()
        file = service.files().update( media_body=media,
                                      fileId=fileid).execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')


def set_driver_cookies(driver,vpn_id=2):
	print("setting cookies")
	try:	
		df= read_sheet(sheet_name="Sheet3")
		# cookies=df[df['vpn_id']==vpn_id].sample(n=1).to_dict(orient='records')[0]['cookies']
		cookies=json.loads(df.sample(n=1).to_dict(orient='records')[0]['cookies'])	
	except Exception as e:
		print("cookie error:",e)
		cookies=[{'domain': '.youtube.com', 'expiry': 1696800781, 'httpOnly': True, 'name': 'LOGIN_INFO', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AFmmF2swRAIgeTSsxUyWhTidfq_qLwbF9J9PjopO7kk3EgLSwG2jdy4CIByzmM0oOgZ13nf_Eun1OkPxaLn3lnMeH1XCaleRY1Td:QUQ3MjNmelQzMDlFSDhjb3REVnp1bGtIN2l2WU1oX2NRRDIxRmNTZmttcnM4TTZueTR3cWlZcG1wT3JJMlNscjZvX3FzT2hla0F2Y3RjWkN4RkFHcm8xTm1iNzMySE82UG5ZekVUNkxiUkZyQXAxdWdxTnVxYnJRc3FySFZ5NlhSNGZlS2VfZVh6MmtuWXVyWWEzRFl0eE9PVmotNmh3N29n'},{'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': False, 'name': 'SID', 'path': '/', 'secure': False, 'value': 'OAjcTQfQ3DWWajAPttwUu1MOMR7-HNujx33PIBs9iZ9qdOftXUuYBT0cDAAOqzLBXpEa5A.'}, {'domain': '.youtube.com', 'expiry': 1696800756, 'httpOnly': False, 'name': 'CONSENT', 'path': '/', 'secure': True, 'value': 'PENDING+759'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': 'HSID', 'path': '/', 'secure': False, 'value': 'ALKicwGR6CrqSgocV'},{'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': 'SSID', 'path': '/', 'secure': True, 'value': 'A9IY-7Y2ccQWGbw_W'},{'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': 'SOCS', 'path': '/', 'secure': True, 'value': 'CAISEwgDEgk0NzEzNjQ0MzgaAmVuIAEaBgiAm9qYBg'}]
	for cookie in cookies:
		# print(cookie)
		driver.add_cookie({'name':cookie['name'],'value':cookie['value']})
	return 


def set_view_bot_cookies(driver,vpn_id=2):
	print("setting cookies")
	try:	
		df= read_sheet(sheet_name="Sheet3")
		# cookies=df[df['vpn_id']==vpn_id].sample(n=1).to_dict(orient='records')[0]['cookies']
		cookies=json.loads(df.sample(n=1).to_dict(orient='records')[0]['view_bot'])	
	except Exception as e:
		print("cookie error:",e)
		cookies=[{"domain": ".growviews.com", "expiry": 1695655400, "httpOnly": False, "name": "tk", "path": "/", "secure": False, "value": "1e1ffa5245d395218a9d246641d5f877bedfdbd6"}, {"domain": ".app.growviews.com", "expiry": 1695676991, "httpOnly": False, "name": "__adroll_fpc", "path": "/", "sameSite": "Lax", "secure": False, "value": "e93fb590d12e2827c885e4f090c027ba-1664119391784"}, {"domain": ".growviews.com", "expiry": 1698679400, "httpOnly": False, "name": "_ga", "path": "/", "secure": False, "value": "GA1.2.1906643159.1664119383"}, {"domain": ".app.growviews.com", "httpOnly": False, "name": "__adroll_consent_params", "path": "/", "sameSite": "Lax", "secure": False, "value": "_l%3Den%26_c%3D1%26_v%3D9%26_tcf%3D2%26iab%3D2%26_e%3Ddeferred_consent%26_s%3D11df716c79e255faa8eebea17374cc2d%26_b%3D2.1%26_a%3D7EUMSJ4ZDVBUNH3OKD5DLM"}, {"domain": ".growviews.com", "expiry": 1665329000, "httpOnly": True, "name": "sessionid", "path": "/", "secure": False, "value": "azq6zlodqoh6wg7ydtfh757f8zv0d5hi"}, {"domain": ".growviews.com", "expiry": 1664205800, "httpOnly": False, "name": "_gid", "path": "/", "secure": False, "value": "GA1.2.1390301675.1664119383"}, {"domain": ".app.growviews.com", "expiry": 1695655391, "httpOnly": False, "name": "__adroll_consent", "path": "/", "sameSite": "Lax", "secure": False, "value": "CPf5He2Pf5He2AAACBENAJCv_____3___wiQAQwAYAAgBCAEMAGAAIAQgAA%237EUMSJ4ZDVBUNH3OKD5DLM"}, {"domain": ".app.growviews.com", "expiry": 1695655391, "httpOnly": False, "name": "__ar_v4", "path": "/", "sameSite": "Lax", "secure": False, "value": "%7C7EUMSJ4ZDVBUNH3OKD5DLM%3A20220925%3A1%7CSVQOJAREMJFV3BSHDIN5AD%3A20220925%3A1%7CWXTTVWKCJRB63EMBTQ4N4H%3A20220925%3A1"}, {"domain": ".growviews.com", "expiry": 1664119443, "httpOnly": False, "name": "_gat_UA-61330030-1", "path": "/", "secure": False, "value": "1"}]
	for cookie in cookies:
		print(cookie)
		driver.add_cookie({'name':cookie['name'],'value':cookie['value']})
	return 

def set_view_grip_cookies(driver,vpn_id=2):
	print("setting cookies")
	try:	
		df= read_sheet(sheet_name="Sheet3")
		# cookies=df[df['vpn_id']==vpn_id].sample(n=1).to_dict(orient='records')[0]['cookies']
		cookies=json.loads(df.sample(n=1).to_dict(orient='records')[0]['view_grip'])	
	except Exception as e:
		print("cookie error:",e)
		cookies=[{"domain": ".viewgrip.net", "expiry": 1698746726, "httpOnly": False, "name": "_ga", "path": "/", "secure": False, "value": "GA1.1.202413009.1664186701"}, {"domain": ".viewgrip.net", "expiry": 1698746726, "httpOnly": False, "name": "_ga_767XEYY4K8", "path": "/", "secure": False, "value": "GS1.1.1664186700.1.1.1664186726.0.0.0"}, {"domain": ".viewgrip.net", "expiry": 1664273122, "httpOnly": False, "name": "_gid", "path": "/", "secure": False, "value": "GA1.2.1017869442.1664186703"}, {"domain": ".viewgrip.net", "expiry": 1664188500, "httpOnly": True, "name": "__cf_bm", "path": "/", "sameSite": "None", "secure": True, "value": ".h1T6niEQPR3emyzymU3tIS00cq8S38PfpvrgsW9Qis-1664186700-0-ATGYzIh5Osf/uke6bYAvc7Yc2mKt55Y0W51V4wK2o4kV1rsm0iYricnTulD1Mgy+rnkMCxNMThQdTGGaZXHvNFNjybTcsk9i9kKsJuAspew3xoCcaQzN1cjSIFhqySEEI0hNaCI0g/rcui8fsI8XeaEU76n0rvrrlp3ysYMphHdg"}, {"domain": ".viewgrip.net", "expiry": 1664186762, "httpOnly": False, "name": "_gat_gtag_UA_97989219_1", "path": "/", "secure": False, "value": "1"}, {"domain": ".viewgrip.net", "expiry": 1671962700, "httpOnly": False, "name": "_gcl_au", "path": "/", "secure": False, "value": "1.1.2091363554.1664186701"}, {"domain": "www.viewgrip.net", "expiry": 1666865100, "httpOnly": False, "name": "PHPSESSID", "path": "/", "secure": False, "value": "ur5q2hcmu3hph27l52ebigio7a"}]
	driver.delete_all_cookies()
	for cookie in cookies:
		# print(cookie)
		driver.add_cookie({'name':cookie['name'],'value':cookie['value']})
	return 



def play_and_sleep(driver):
	try:
		if driver.execute_script(" return document.getElementsByTagName('video')[0].paused")==True:
			actions = ActionChains(driver)
			print("paused")
			actions.send_keys(Keys.SPACE).perform()
		duration= driver.execute_script(" return document.getElementsByTagName('video')[0].duration")
		duration=int(duration)
		print("video duration" ,duration)
		random_duration=random.randint(duration,duration+5)
		time.sleep(random_duration)
	except Exception as e:
		print(e)
	return 

def play_and_skip_ads(driver):
	try:
		if driver.execute_script(" return document.getElementsByTagName('video')[0].paused")==True:
			actions = ActionChains(driver)
			print("paused")
			actions.send_keys(Keys.SPACE).perform()
		duration= driver.execute_script(" return document.getElementsByTagName('video')[0].duration")
		duration=int(duration)
		print("Ad duration" ,duration)
		random_duration=random.randint(duration//2,duration)
		time.sleep(random_duration)
		if driver.execute_script("return document.getElementsByClassName('ytp-ad-skip-button ytp-button')[0].childElementCount")>0:
			driver.execute_script("return document.getElementsByClassName('ytp-ad-skip-button ytp-button')[0].click()")
			print("skipped add")
	except Exception as e:
		print(e)
	return 




def play_via_channel_page(driver,video_url,channel_url):
	video_id=video_url.split("watch?v=")[1]
	url=channel_url+"/search?query="+video_id
	driver.get(url)
	# driver.save_screenshot("channel_load.png")
	# upload_basic("channel_load.png")
	vide_elements=driver.execute_script("return document.getElementsByClassName('yt-simple-endpoint style-scope ytd-video-renderer')")
	if len(vide_elements)>0:
		print("via channel_url")
		for i in range(0,len(vide_elements)):
			if video_id in driver.execute_script("return document.getElementsByClassName('yt-simple-endpoint style-scope ytd-video-renderer')["+str(i)+"].href"):
				print("video by channel search")
				# driver.save_screenshot("channel_search.png")
				# upload_basic("channel_search.png")
				driver.execute_script("return document.getElementsByClassName('yt-simple-endpoint style-scope ytd-video-renderer')["+str(i)+"].click()")
				break
	else:
		print("direct url")
		driver.get(video_url)

	return 

def play_via_youtube_search(driver,video_url,channel_url):
	video_id=video_url.split("watch?v=")[1]
	url="https://www.youtube.com/results?search_query="+video_id
	driver.get(url)
	vide_elements=driver.execute_script("return document.getElementsByClassName('yt-simple-endpoint style-scope ytd-video-renderer')")
	if len(vide_elements)>0:
		print("via youtube search")
		for i in range(0,len(vide_elements)):
			if video_id in driver.execute_script("return document.getElementsByClassName('yt-simple-endpoint style-scope ytd-video-renderer')["+str(i)+"].href"):
				print("video by youtube search")
				driver.execute_script("return document.getElementsByClassName('yt-simple-endpoint style-scope ytd-video-renderer')["+str(i)+"].click()")
				break
	else:
		print("direct url")
		driver.get(video_url)

	return 




def direct_play(driver,video_url,channel_url):
	driver.get(video_url)
	return


def play_via_embeded(driver,video_url,channel_url):

	return

def play_via_proxy_browser(driver,video_url,channel_url):
	url="https://www.croxyproxy.com/"
	driver.get(url)
	time.sleep(2)
	driver.execute_script("return document.getElementById('url').value='"+video_url+"'")
	time.sleep(5)
	driver.find_element(By.ID,"requestSubmit").click()

	return


def get_random_video(only_video=False):
	df=read_sheet(sheet_name="Sheet1")
	row=df.sample(n=1).to_dict(orient='records')[0]
	if only_video:
		return row['video']
	else:
		return row['video'],row['channel']




def turn_on_vpn(driver):
	try:
		driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html")
		time.sleep(3)

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
		# driver.save_screenshot("bits.png")
		# upload_basic("bits.png")
	except:
		print("vpn error")
		random_vpn=0
	return random_vpn

def get_user_agent():
	df=read_sheet(sheet_name="Sheet2")
	try:
		user_agent=df.sample(n=1).to_dict(orient='records')[0]['useragent']
	except:
			user_agent=None
	return user_agent













