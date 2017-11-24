#  http://ieeexplore.ieee.org/xpl/downloadCitations?citations-format=citation-only&download-format=download-bibtex&recordIds=8110474
import res 

# 
# Maybe think of removing some redundant code between scrapers..
# such as user agents -> times for waiting
# maybe also 
# They do contain different data in their resource files though...

def getRandomUserAgent():
    return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING))]

def requestBibtex(url , headers, parameters):
	try:

		req = requests.get(url, params=params , headers=headers)

		soup = BeautifulSoup(req.text, "html.parser")

		# check how to parse returned data

def Main():
	citation_id = 0;

	userAgent = getRandomUserAgent()

	url = res.IEEE_URL_START

	params = {
			res.IEEE_URL_PARAM_1 : res.IEEE_URL_PARAM_1_VALUE,
			res.IEEE_URL_PARAM_2 : res.IEEE_URL_PARAM_2_VALUE,
			res.IEEE_URL_PARAM_3 : citation_id
	}
	headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': userAgent
	}
	values = requestBibtex(url, params, headers)




Main()