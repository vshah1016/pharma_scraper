from bs4 import BeautifulSoup
import requests
from decimal import Decimal

#defining a constant map so that we can map how many 0's to add for a M or B
d = {
    'M': 6,
    'B': 9,
    'k': 3,
}

#making a function that will convert numbers like "53.2M" to 53,200,000 and "4.2B" to 4,200,000,000
def text_to_num(text):
        if text[-1] in d:
            num, magnitude = text[:-1], text[-1]
            return Decimal(num) * 10 ** d[magnitude]
        else:
            return Decimal(text)


def scrape(ticker):
    try:
        #defining the stats we want to scrpe
        key_stats_on_main =['Market Cap', '1y Target Est',]
        key_stats_on_stat =['52 Week High', '52 Week Low', 'Revenue', 'Total Cash', 'Total Debt', 'Net Income Avi to Common',]

        #the url for both of the different screens we want to scrape from
        summary_page_url = "https://finance.yahoo.com/quote/{0}?p={0}".format(ticker)
        statistics_page_url = "https://finance.yahoo.com/quote/{0}/key-statistics?p={0}".format(ticker)

        #array that will eventually hold all data wanted
        #will be held in the following order
        #[market cap, target, yearly high, yearly low, revenue, cash, debt, net income]
        scraped_data = []

        #getting html data from the summary page of the stock and parsing it with BeautifulSoup
        soup = BeautifulSoup(requests.get(summary_page_url).text, 'html.parser')

        #iterating through all wanted stats and looking at that row, finding the parent tags and finding the value then it gets appended to the list
        for stat in key_stats_on_main:
            scraped_data.append(text_to_num(soup.find(text=stat).find_parent('tr').find_all('td')[1].contents[0].contents[0]))

        #parsing the statistics page of the ticker
        soup = BeautifulSoup(requests.get(statistics_page_url).text, 'html.parser')

        #iterating through all wanted stats and looking at that row, finding the parent tags and finding the value then it gets appended to the list
        #we have to catch all of the N/A for the data that Yahoo Finance does not have on hand
        for stat in key_stats_on_stat:
            value = soup.find(text=stat).find_parent('td').find_parent('tr').find_all('td')[1].contents[0]
            try:
                scraped_data.append(value.contents[0])
            except:
                scraped_data.append(text_to_num(value))

        #returns the data that we have scraped from yahoo finance
        return scraped_data
    except:
        return scrape(ticker)