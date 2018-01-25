# used for scraping Collection of ComputerScience Bibliography
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

 # format of request/query ^^
 # query : @string
 # field : 
 # start : @position.. so if you want 2nd page and maxnum =400 -> start should be 401
 # year : @specific year
 # since : @year
 # before : @year
 # results : bibtex
 # maxnum : 400
 # sort : year
 # online : off
 # x : 7
 # y : 11

# PUT ALL LITERAL DATA STRINGS IN RES FILE...
def cleanMe(html):
    soup = BeautifulSoup(html, "html.parser") # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text



def getRequest(url, params, headers):
	try:
		# May have forgotten headers here..
		req = requests.get(url, params=params, headers=headers)
		
		#insert 404 response code here		
		#if req.status_code == 404:
		#	moveOn = True
		soup = BeautifulSoup(req.text, "html.parser")

		myBibtexPres = soup.findAll("pre",{"class" : "bibtex"})
		# print(myBibtexPres)
		# print(myBibtexPres[0].text)

		return myBibtexPres
	except Exception as e:
		print(e)
		#moveOn = True
		return None

def getRandomMidDelay():
    return random.randint(6,15)

def getRandomUserAgent():
    return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING)-1)]


def getNamesData():
    with open("finalNames.txt","r") as lines:
        result = []
        for line in lines:
            result.append(line)
    return result


#  maybe wait 30 seconds per request... because we can get 400 articles per request

def Main():
	path_file_test = "data_cid_data.txt"
	complete_path_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), path_file_test)
	file = open(complete_path_data, "a")
	# https://liinwww.ira.uka.de/csbib/?query=%22Hello%22 

	names = getNamesData()

	userAgent = getRandomUserAgent()

	param_start = 1
	param_maxnum = 400

	#moveOn = False
	# Only goes up to 1000 in search 
	url = "https://liinwww.ira.uka.de/csbib/"
	# will need to add to this
	params = {
			'query' : names[0],
			'results' : 'bibtex',
			'sort' : 'year',
			'start' : str(param_start) ,
			'maxnum' : str(param_maxnum),
			}
	headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': userAgent
	}
	# for name in names:
	i = 3461
	try :
		while i < len(names):
			#	update 1000 to a constant somewhere
			#while moveOn == False & param_start < 1000:
			while param_start <1000:	
				# This is inefficient... Clean this..
				
				params = {
					# 'query' : name,
					'query' : names[i],
					'results' : 'bibtex',
					'sort' : 'year',
					'start' : str(param_start) ,
					'maxnum' : str(param_maxnum),
					}
				headers['user-agent'] = getRandomUserAgent()	
				# at the end of this while.. I would need to reinitialise moveOn to true.. or maybe even before this while loop
				bibtexData = getRequest(url, params, headers)
				for bib in  bibtexData:
					# Going to solve the sarah problem here by preprocessing the entries
					#sys.exit()
					
					if bib.text[0:16] != res.HOME_PAGE_STRING2: 
						file.write(bib.text)
						
				param_start += param_maxnum
				# Need to add a delay				
				time.sleep(getRandomMidDelay())
				# file.write(str(req.text)) 
				# bibtexDatabase = parseHTMLForBibtex(bibtexData)
				# print(bibtexDatabase)
				# moveOn = True
				#  not sure what this should return
			i += 1
			param_start = 1
	except Exception as e:
		print(e)
		print(names[i])

	



Main()
