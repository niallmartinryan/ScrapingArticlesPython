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


def getRequest(url, params):
	req = requests.get(url, params=params)

	soup = BeautifulSoup(req.text, "html.parser")

	myBibtexPres = soup.findAll("pre",{"class" : "bibtex"})
	# print(myBibtexPres)
	print(myBibtexPres[0])


def getRandomMidDelay():
    return random.randint(15,25)
    
def getRandomUserAgent():
    return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING))]



def Main():
	name_file_test = "data_cid_data.txt"
	complete_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name_file_test)
	file = open(complete_path, "w")
	
	# https://liinwww.ira.uka.de/csbib/?query=%22Hello%22 
	# heheheheh

	url = "https://liinwww.ira.uka.de/csbib/"
	# will need to add to this
	params = {'query' : 'angela',
			'results' : 'bibtex',
			'sort' : 'year'
			}
	headers = {

	}
	for
	getRequest(url, params)
	

	# file.write(str(req.text))



Main()