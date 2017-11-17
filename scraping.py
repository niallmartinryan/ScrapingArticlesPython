# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())
import sys
import os.path

# needed in order to import resources file.. and any other file rip..
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '\\resources\\')


import resources as res
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import requests

#print(resources.sexy_url)
# import resources.resources.ScrapingPython 

# how do I want to actually want to download/store all of this stuff.. Do I want to grab all the data-cids and store them somewhere..
#  or Do I want to dynamically have threads downloading stuff as data-cids are acquired 
# 

# KEEP YOUR NAMING OF VARIABLES CONSISTENT YOU BUMBLING FOOL  


# look up about constants in python..
url = "https://scholar.google.com/scholar?=0&q=c&hl=en&as_sdt=0,5" 
# url = res.GOOGLE_SCHOLAR_MAIN_PAGE
searchIndex = "0"
# searchCriteria = ""
testSearchCriteria = "a"
# url = (res.GOOGLE_SCHOLAR_SEARCH_START + searchIndex + res.GOOGLE_SCHOLAR_SEARCH_MIDDLE + 
        # testSearchCriteria + res.GOOGLE_SCHOLAR_SEARCH_END)
# save_path = "C:/Users/niall/Documents/A college/FourthYear/dissertation/ScrapingPython/testData/"
name_file_test = res.DATA_CID_FILE_NAME


# Some stuff happening here
complete_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name_file_test)
file = open(complete_path, "w")



urls = [url]
visited = [url]

# aboutResults = soup.find_all("div", class_="gs_ab_mdw")

# MaxNumResults =         # This will be the result we grab from beauSoup and then -10 for the index of that page  
print(urls[0])
while len(urls) > 0:
    
    # do some stuff here

    # while 
        try:
            # url = 'https://scholar.google.pl/citations?view_op=search_authors&mauthors=label:security'

            # request_headers = {
            #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #     'accept-encoding': 'gzip, deflate, br',
            #     'accept-language': 'en-US,en;q=0.8',
            #     'upgrade-insecure-requests': '1',
            #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
            # } 
            # s = requests.Session()
            # s.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #     'accept-encoding': 'gzip, deflate, br',
            #     'accept-language': 'en-US,en;q=0.8',
            #     'upgrade-insecure-requests': '1',
            #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
            # })
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
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
            }
            r = requests.get(url, headers = headers)

            text = r.text.encode("utf-8")
            soup = BeautifulSoup(text,"html.parser")
            print(r.text[0:1000])
            
            file.write(r.text)
            file.close()
            mydivs = soup.findAll("div", { "class" : "gs_r gs_or gs_scl" })


            print(soup.findAll(res.DATA_CID_SEARCH_STRING))

            print(mydivs[0].encode("utf-8"))
                # htmltext = urllib.request.urlopen(urls[0]).read()
        except Exception as e:
           print(e)      
        
        # soup = BeautifulSoup(htmltext,"html.parser")    
        urls.pop(0)
        # scrapeKChars = soup.prettify()[1:1000]

        # file.write(scrapeKChars)

        # file.close()
        #print(soup.prettify()[0::1])
        # print(soup.findAll(res. DATA_CID_SEARCH_STRING))





        # When scraping the "data-cid"s May need to disregard the first one as it doesnt have a element..aka. no = afterwards
