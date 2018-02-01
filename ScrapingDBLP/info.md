In Dblp they allow you to download an authors citations as bibtex,
So I plan to scrape firstly all the authors available on their site,
which shouldnt take too long as they store them quite compactly per page

Then running through each author, going to the appropriate page and downloading it as bibtex or scraping the page itself

May have just downloaded the entire library in xml format.. working on converting it to bibtex

Technical--

url for names = dblp.uni-trier.de/pers?prefix=A
url for names pos = dblp.uni-trier.de/pers?pos=1

going to use the second one because I can stop when pos gets to the end.

after all the authors are collected I can begin looking for their bibtex records using a url like

anywhere an "@" symbol, represents a place holder for data from the name
If the name contains a dot, then an "=" must be placed where it would be

dblp.uni-trier.de/pers/hb/@FirstLetterOfAuthor/@FirstNameBeforeComma:@NameAfterComma  with .html if needed

instead of parsing this.. we can grab the html and write it by using the following url

dblp.uni-trier.de/pers/tb2/@FirstNameBeforeComma:@NameAfterCommaSeparatedByUnderscores.bib
