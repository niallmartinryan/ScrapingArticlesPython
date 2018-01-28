# Going to attempt to scrape a single Id just to see resukts

import sys
import os.path
import time

import res
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
#import urllib.URLopener
import requests
import random


# When cleaning up the code, make sure to reduce redundancy everywhere
def getRandomStandardDelay():
	return random.randint(10,20)

def getRandomUserAgent():
	return res.USER_AGENT_STRING[random.randint(0, len(res.USER_AGENT_STRING)-1)]








def Main():
		
	url = res.TEST_LINK_STRING
	name_file = res.FILE_NAME
	complete_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name_file)
	file = open(complete_path, "a")

	
	try:
		userAgent = getRandomUserAgent()
		headers = { 'Connection' : 'keep-alive',
			'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*,q=0/8',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.8',
			'upgrade-insecure-requests': '1',
			'user-agent': userAgent
			}
		
		session = requests.Session()
	
		#req1 = session.get(url, headers=headers)

		req2 = session.get(url, headers=headers)
		
		with open("testFile.txt", "a") as save:
			save.write(req2.content)

		#urllib.urlretrieve(url, name_file)
		#testFile = urllib.URLopener()
		#testFile.retrieve(url, name_file)
		#r = requests.get(url, headers=headers)
		#print(r)
		#file.write(r.text)

	except Exception as e:
		print(e)
	return None








Main()
