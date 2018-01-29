#  https://dl.acm.org/citation.cfm?doid=965400.111112
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


# comment this code ;)

def getRandomUserAgent():
    return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING)-1)]

def getRequest(url, params, headers, target_path):
	try:
		
		# print(url)
		req = requests.get(url, params=params, headers=headers)
		# req = requests.get(url, headers=headers)
		# print(req)
		return (req.text)
		# return str(req.content)
		# soup = BeautifulSoup(req.text, "html.parser")
		# handle = open(target_path, "a")
		# for chunk in req.iter_content(chunk_size=512):
		# 	if chunk:
		# 		handle.write(chunk)
		# return req.text

	except Exception as e:
		print(e)
		return None

def getRandomShortDelay():
    return random.randint(2,10)

def Main():
	
	name_file_test = res.FILE_NAME

	complete_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),name_file_test )
	file = open(complete_path, "a")

	userAgent = getRandomUserAgent()
	# name_file_test = 
	target_path = "data.txt"
	url = res.URL_START
	index = 49533
	max_index = 3164405
	params = {
			res.URL_PARAM_1 : str(index),
			res.URL_PARAM_2 : res.URL_PARAM_2_VALUE,
			res.URL_PARAM_3 : res.URL_PARAM_3_VALUE,
			'stream' : 'True'
	}

	headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8', 
            'upgrade-insecure-requests': '1',
            'user-agent': userAgent
	}
	try:
		while index < max_index:
			stuff = getRequest(url, params, headers, target_path)
			if stuff is None:
				print("found none")
			else:
				file.write(stuff)
			headers['user-agent'] = getRandomUserAgent()
			index += 1
			params[res.URL_PARAM_1] = str(index)
			time.sleep(getRandomShortDelay())
	except KeyboardInterrupt:
		print("index = "+ str(index))
Main()
