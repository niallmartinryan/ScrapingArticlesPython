#  http://ieeexplore.ieee.org/xpl/downloadCitations?citations-format=citation-only&download-format=download-bibtex&recordIds=8110474
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
# 
# Maybe think of removing some redundant code between scrapers..
# such as user agents -> times for waiting
# maybe also 
# They do contain different data in their resource files though...

def getRandomShortDelay():
    return random.randint(2,10)

def getRandomUserAgent():
    return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING)-1)]

def requestBibtex(url , params, headers):
	try:

		req = requests.get(url, params=params , headers=headers)

		text = cleanMe(req.text)
		return text
	except Exception as e:
		print(e)
		return None
		# check how to parse returned data

# reference this.. or tidy it up
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

def Main():

	name_file_test = res.FILE_NAME

	complete_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),name_file_test )
	file = open(complete_path, "a")


	citation_id = 4011900;

	maxCitation_id = 8011901
	userAgent = getRandomUserAgent()

	url = res.IEEE_URL_START

	params = {
			res.IEEE_URL_PARAM_1 : res.IEEE_URL_PARAM_1_VALUE,
			res.IEEE_URL_PARAM_2 : res.IEEE_URL_PARAM_2_VALUE,
			res.IEEE_URL_PARAM_3 : str(citation_id)
	}
	headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': userAgent
	}
	try:
		while citation_id <= maxCitation_id 
			values = requestBibtex(url, params, headers)
			# print(values)
			file.write(values)

			headers['user-agent'] = getRandomUserAgent()
			citation_id +=1
			params[res.IEEE_URL_PARAM_3] = str(citation_id)
			time.sleep(getRandomShortDelay())	
	except KeyboardInterrupt:
		print("citation_id : "+ citation_id)

Main()