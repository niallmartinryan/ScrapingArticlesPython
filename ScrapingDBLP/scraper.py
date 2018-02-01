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
import string


def getRandomShortDelay():
	return random.randint(2,10)

def getRandomMidDelay():
	return random.randint(2,12)

def getRandomUserAgent():
	return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING)-1)]


def getNames(url, params, headers, file):
	# Dont need these anymore as pags are indexed. Upper case alphabet string = "ABCD..YZ"
	# alpha = string.ascii_uppercase
	# alphaCounter = 0
	
	

	personCounter = 1
	magicEndNumber = 2057018
	# page are incremented by 300 which is the number of authors that are shown per page
	increment = 300

	authors = []
	try:
		while personCounter < magicEndNumber:
			print(str(personCounter) + "\n" )
			testURL = res.URL_ENTRIES_STRING
			params['pos'] = personCounter
			req = requests.get(testURL,params=params, headers=headers)	
			#print req.text
			soup = BeautifulSoup(req.text, "html.parser")
		
			myDivs = soup.findAll("div", {"class": "column min20"})
			#print(myDivs[0])
			#print(myDivs[1])		
			for div in myDivs:
				lis = div.findAll('li')
				for li in lis:
					file.write(li.text + "\n") 
					authors.append(li.text)
			headers['user-agent'] = getRandomUserAgent()
			personCounter = personCounter + increment
			time.sleep(getRandomShortDelay())
		print(personCounter)	
		return authors	
	except Exception as e:
		print(personCounter)
		print(e)
		#return authors
	#while personCounter < magicEndNumber:
		#request the page

def getBibtex(authors, params, headers, file):
	try:
		for author in authors:
			print(author)
			url = urlBuilder(author)
			session = requests.Session()
			req = session.get(url, params=params, headers=headers)
			with open("data.txt", "a") as save:
				save.write(req.text+ "\n")		
			#req = requests.get(url,	params=params, headers=headers)			
			headers['user-agent'] = getRandomUserAgent()
			time.sleep(getRandomMidDelay())
	except Exception as e:
		print(author)
		print(e)

def urlBuilder(author):
	baseURL = res.URL_AUTHOR_BIBTEX
	baseURL = baseURL + str(author[0].lower()) + "/"
	splitAuthor = author.split(',')
	first = splitAuthor[0]
	if len(splitAuthor) == 1:
		second = ""
	else:	
		second = splitAuthor[1]
	first = first.replace('.', '=')
	first = first.replace('-', '=')
	first = first.replace(' ', '_')
	second = second.replace('.', '=')
	second = second.replace('-', '=')
	second = second.replace(' ', '_')
	sub = second[1:]	
	 
	baseURL = baseURL + first + ":" +str(sub) + ".bib"
	
	return baseURL	

	#if "." in splitAuthor[0]:
	#	splitFirstName = splitAuthor[0].split(".")
	#	baseURL = baseURL + str(splitAuthor[0]) + "="
	#	if "" is splitFirstName:
	#		baseURL = baseURL + ":"
	#	else:
	#		baseURL = baseURL + str(splitFirstName[1]) + ":"
	#else:
	#	baseURL = baseURL + str(splitAuthor[0]) + ":"
	#
	#baseURL = baseURL
	





def Main():
	name_file = res.FILE_NAME
	author_file = res.FILE_AUTHORS
	
	complete_path_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), name_file)
	complete_path_authors = os.path.join(os.path.dirname(os.path.abspath(__file__)), author_file)	

	file = open(complete_path_data, "a")
	authors_file = open(complete_path_authors, "a")
	
	userAgent = getRandomUserAgent()

	url = res.URL_ENTRIES_STRING
	params = {
		'pos' : '1'
	}
	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.8',
		'upgrade-insecure-requests': '1',
		'user-agent': userAgent	
	}
	
	names = getNames(url, params, headers, authors_file)		
	print("finished collecting names")
	input("Press Enter to Continue..")

	getBibtex(names, params, headers, file)	
	#testString = "O.-Larnnithipong, Nonnarit"
	#urlBuilder(testString)
	print("finished")
	return None


Main()
