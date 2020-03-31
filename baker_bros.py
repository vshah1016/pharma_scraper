import requests
from bs4 import BeautifulSoup

def is_entry(href):
  return "&sortBy=PeriodOfReport&chartDisplay=90" in href

#making our constat variables to make our page source review
baker_bros_link = "http://www.j3sg.com/Reports/Stock-Insider/Generate-Institution-Portfolio.php?institutionid=4698&viewArchive=no&archiveDateIn=&DV=yes"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0'}

#pointing out page source to BeautifulSoup
soup = BeautifulSoup(requests.get(baker_bros_link, headers = headers).text, 'html.parser')

#maps through the list of all <a> </a> tags with the tickers in them to make them into just the ticker
all_holdings = list(map(lambda entry: entry.contents[0], soup.findAll('a', href=is_entry)))

def get_baker_holdings():
    return all_holdings