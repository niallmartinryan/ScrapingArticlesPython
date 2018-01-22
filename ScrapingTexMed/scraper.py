# scraper for TexMed which is an interface to PubMed
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
    return random.randint(2,15)

def getRandomUserAgent():
    return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING)-1)] 

def scrapeBibtexFromHTML(html):

	soup = BeautifulSoup(html, "html.parser")

	soup.find("PRE")
#	will need to remove the first line of the text within Pre 

def requestBibtex(url, params, headers):
	try:
		req = requests.get(url, params=params, headers=headers)
		soup = BeautifulSoup(req.text, "html.parser")
		# find pre tag within html
		bib = soup.find('pre').text
		# parse out the actual bib entry
		newBib = bib[bib.find("@")+1:]
		print(newBib)
		return newBib
	except Exception as e:
		print(e)
		return None



def Main():
	fileName = res.FILE_NAME
	complete_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),fileName )
	file = open(complete_path, "a")

	userAgent = getRandomUserAgent()

	url = res.URL_START_STRING
	citationID = 1

	maxCitationID = 29162941

	params = {
			res.URL_PARAM_1 : str(citationID)
	}
	headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': userAgent
	}
	# req = requestBibtex(url, params, headers)
	# soup = BeautifulSoup(req.text, "html.parser")

	# bib = soup.find('pre').text
	# print(bib)
	# newBib = bib[bib.find("@")+1:]
	# print(newBib)
	
	try:
		while citationID <= maxCitationID:
			req = requestBibtex(url, params, headers)
			file.write(req)
			citationID += 1
			headers['user-agent'] = getRandomUserAgent()
			params[res.URL_PARAM_1] = str(citationID)
			time.sleep(getRandomShortDelay())
	except KeyboardInterrupt:
		print("citationID = " + citationID)  

Main()
