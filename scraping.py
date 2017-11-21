# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())
import sys
import os.path
import time
# needed in order to import resources file.. and any other file rip..
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '\\resources\\')


import res as res
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import requests
import random

def getRandomMidDelay():
    return random.randint(15,25)

def getRandomShortDelay():
    return random.randint(1,5)

def getRandomStandardDelay():
    return random.randint(20, 40)

def getRandomUserAgent():
    return res.USER_AGENT_STRING[random.randint(0,len(res.USER_AGENT_STRING))]

def getBibtexText1(data_cid ):
    url = (res.SCHOLAR_BIBTEX_LINK_START + str(data_cid) + res.SCHOLAR_BIBTEX_LINK_END)
    print(url)
    try :
        userAgent = getRandomUserAgent()

        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': userAgent
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        r = requests.get(url, headers = headers)
        text = r.text.encode("utf-8")
        soupA = BeautifulSoup(text,"html.parser")
        # print(text)
        # Use the resources page...
        myLinks = soupA.findAll("a", {"class"  : "gs_citi"} )
        myLink = myLinks[0]['href']
        return myLink
        
    except Exception as e:
       print(e)   
    return None

def getBibtexText2(url):
    print(url)
    try :
        userAgent = getRandomUserAgent()
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': userAgent
        }
        r = requests.get(url, headers = headers)
        # well hmmm
        text = r.text.encode("utf-8").decode("utf-8") 
        print(text)
        # file.write(text)
        return(text)
        # Use the resources page...
    except Exception as e:
       print(e)   
    return None

def getNamesData():
    with open("finalNames.txt","r") as lines:
        result = []
        for line in lines:
            result.append(line)
    return result

# if you get a chance.. update this function properly - > parameters + constants..
def getBibtexURL(url):
    data_cid_list = []
    try:
        userAgent = getRandomUserAgent()
        # url = 'https://scholar.google.pl/citations?view_op=search_authors&mauthors=label:security'

        # request_headers = {
        #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'en-US,en;q=0.8',
        #     'upgrade-insecure-requests': '1',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        # } 
        # s.get(url, headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'en-US,en;q=0.8',
        #     'upgrade-insecure-requests': '1',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        # })

        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': userAgent
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            #  maybe try updating the header inorder to change agent..
        }
        r = requests.get(url, headers = headers)

        text = r.text.encode("utf-8")
        soup = BeautifulSoup(text,"html.parser")
        # print(r.text[0:1000])
        
        # file.write(r.text)
        # file.close()
        mydivs = soup.findAll("div", { "class" : "gs_r gs_or gs_scl" })
        for div in mydivs:
            # print(div['data-cid'].encode("utf-8"))
            myThingy = div['data-cid'].encode("utf-8")
            # what the actual is happening here..
            # print(myThingy.decode("utf-8"))
            data_cid_list.append(myThingy.decode("utf-8"))
        # htmltext = urllib.request.urlopen(urls[0]).read()
        # time.sleep(sleepConstantTime + getRandomShortDelay)
        return data_cid_list
        #  going to have to have a timeout of 10-20 seconds
    except Exception as e:
       print(e)
       return None    
    # When scraping the "data-cid"s May need to disregard the first one as it doesnt have a element..aka. no = afterwards
#print(resources.sexy_url)
# import resources.resources.ScrapingPython 

# how do I want to actually want to download/store all of this stuff.. Do I want to grab all the data-cids and store them somewhere..
#  or Do I want to dynamically have threads downloading stuff as data-cids are acquired 
# 

# KEEP YOUR NAMING OF VARIABLES CONSISTENT YOU BUMBLING FOOL  


# look up about constants in python..
# url = "https://scholar.google.com/scholar?=0&q=c&hl=en&as_sdt=0,5" 
# url = res.GOOGLE_SCHOLAR_MAIN_PAGE
def Main():
    names = getNamesData()
    searchIndex = "0"
    # searchCriteria = ""
    testSearchCriteria = "a"
    url = (res.GOOGLE_SCHOLAR_SEARCH_START + searchIndex + res.GOOGLE_SCHOLAR_SEARCH_MIDDLE + 
            testSearchCriteria + res.GOOGLE_SCHOLAR_SEARCH_END)
    # save_path = "C:/Users/niall/Documents/A college/FourthYear/dissertation/ScrapingPython/testData/"
    name_file_test = res.DATA_CID_FILE_NAME

    # Some stuff happening here
    complete_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name_file_test)
    file = open(complete_path, "a")

    # put this in resources later
    sleepConstantTime = 12


    # urls = [url]
    # visited = [url]

    # aboutResults = soup.find_all("div", class_="gs_ab_mdw")

    maxNumResults = 0      # This will be the result we grab from beauSoup and then -10 for the index of that page  
    # print(urls[0])
    i = 0   # increment/ index of pages
    # while len(urls) > 0:
    while i <= maxNumResults: 
        # do some stuff here
        print(url)
        data_cid_list = getBibtexURL(url)
        print(data_cid_list)
        for dataCid in data_cid_list:
            time.sleep(getRandomStandardDelay())
            reqUrl = getBibtexText1(dataCid)
            # maybe I should write to the file after this.. instead of auto doing it in the file
            time.sleep(getRandomStandardDelay())
            file.write(getBibtexText2(reqUrl))

        i += 10
        index = str(i)
        url = (res.GOOGLE_SCHOLAR_SEARCH_START + index + res.GOOGLE_SCHOLAR_SEARCH_MIDDLE + 
                testSearchCriteria + res.GOOGLE_SCHOLAR_SEARCH_END)
        time.sleep(getRandomStandardDelay())
    # while i <= maxNumResults:
        # soup = BeautifulSoup(htmltext,"html.parser")    
        # urls.pop(0)
        # scrapeKChars = soup.prettify()[1:1000]

        # file.write(scrapeKChars)

        # file.close()
        #print(soup.prettify()[0::1])
        # print(soup.findAll(res. DATA_CID_SEARCH_STRING))
    # link = getBibtexText1(data_cid_list[0])
    # bib = getBibtexText2(link)
    # extraRandomTime = getRandomMidDelay()
    # time.sleep(sleepConstantTime + extraRandomTime)
Main()



# should I try to dyanamically change my ip address/// and perhaps run some threading over this??
# This method will use the data-cid value to request the bibtexHtml
