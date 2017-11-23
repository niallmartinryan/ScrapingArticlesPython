# used for scraping Collection of ComputerScience Bibliography
import sys
import os.path
import time

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

def getRequest(url, params, headers):
	try:
		req = requests.get(url, params=params)

		soup = BeautifulSoup(req.text, "html.parser")

		myBibtexPres = soup.findAll("pre",{"class" : "bibtex"})
		# print(myBibtexPres)
		# print(myBibtexPres[0])
		return myBibtexPres
	except Exception as e:
		# print(e)
		moveOn = true
		return None

def getRandomMidDelay():
    return random.randint(15,25)

def getRandomUserAgent():
    return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING))]


def getNamesData():
    with open("finalNames.txt","r") as lines:
        result = []
        for line in lines:
            result.append(line)
    return result

def parseHTMLForBibtex(html):
	



def Main():
	path_file_test = "data_cid_data.txt"
	complete_path_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), path_file_test)
	file = open(complete_path_data, "w")
	# https://liinwww.ira.uka.de/csbib/?query=%22Hello%22 

	names = getNamesData()

	userAgent = getRandomUserAgent()

	param_start = 1
	param_maxnum = 400

	moveOn = false
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
	while moveOn == false:
		
		params = {
			# 'query' : name,
			'query' : names[0],
			'results' : 'bibtex',
			'sort' : 'year',
			'start' : str(param_start) ,
			'maxnum' : str(param_maxnum),
			}	
	# at the end of this while.. I would need to reinitialise moveOn to true.. or maybe even before this while loop
		bibtexData = getRequest(url, params, headers)
		param_start += param_maxnum 

	


	# file.write(str(req.text))



Main()