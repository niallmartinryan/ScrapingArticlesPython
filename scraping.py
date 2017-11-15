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

#print(resources.sexy_url)
# import resources.resources.ScrapingPython 



# look up about constants in python..
url = res.GOOGLE_SCHOLAR_MAIN_PAGE
# save_path = "C:/Users/niall/Documents/A college/FourthYear/dissertation/ScrapingPython/testData/"
name_file_test = res.DATA_CID_FILE_NAME


# Some stuff happening here
complete_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name_file_test)
file = open(complete_path, "w")



urls = [url]
visited = [url]

while len(urls) > 0:
        try:
           htmltext = urllib.request.urlopen(urls[0]).read()
        except:
           print(urls[0])      

        soup = BeautifulSoup(htmltext,"html.parser")    
        urls.pop(0)
        scrapeKChars = soup.prettify()[1:1000]

        file.write(scrapeKChars)

        file.close()
        #print(soup.prettify()[0::1])
        print(soup.findAll(res. DATA_CID_SEARCH_STRING))



        # When scraping the "data-cid"s May need to disregard the first one as it doesnt have a element..aka. no = afterwards
