# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import os.path
import test



# look up about constants in python..
url = "http://scholar.google.com"
save_path = "C:/Users/niall/Documents/A college/FourthYear/dissertation/ScrapingPython/testData/"
name_file_test = "data_cid.txt"


complete_path = os.path.join(save_path, name_file_test)
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
        print(soup.findAll('data-cid'))



        # When scraping the "data-cid"s May need to disregard the first one as it doesnt have a element..aka. no = afterwards
