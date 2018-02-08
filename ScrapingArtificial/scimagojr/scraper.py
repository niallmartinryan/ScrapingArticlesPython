# Scraping Artificial Journal names from scimagojr
import sys
import os.path
import time
import res
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import requests
import random

def getRandomShortDelay():
	return random.randint(2,10)

def getRandomUserAgent():
	return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING)-1)]

def getTitles(url, params, headers,file, maxPageNum):
	try:
		counter = 1
		while counter <= maxPageNum:
			params['page'] = counter
			req = requests.get(url, params=params, headers=headers)
			soup = BeautifulSoup(req.text, "html.parser")
			#print(req.text)
			myTitles = soup.findAll(title ="view journal details")
			for title in myTitles:
				print(title.text)

	except Exception as e:
		return None
		#chamge this later

def Main():
	name_file = res.FILE_NAME
	complete_path_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), name_file)
	file = open(complete_path_data, "a")

	userAgent = getRandomUserAgent()

	url = res.URL_STRING
	maxPageNum = res.MAX_PAGE_NO  
	
	params = {
		'page' : '1',
		'total_size' : '28606'
	}
	
	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.8',
		'upgrade-insecure-requests': '1',
		'user-agent': userAgent	
	}

	getTitles(url,params,headers, file, maxPageNum)

	




Main()

