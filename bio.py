import requests
from datetime import date, timedelta, datetime
import json


def getEntries(days):
    #establish web session
    session = requests.session()

    #set constants
    site_url = "http://www.biopharmcatalyst.com/calendars/pdufa-calendar"
    headers = {
        'Host': 'www.biopharmcatalyst.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0',
        'Referer': 'https://www.biopharmcatalyst.com/',
    }

    #get cookie to aviod csrf
    source_code = session.get(site_url, headers=headers)
    headers['Cookie'] = str({**session.cookies.get_dict('www.biopharmcatalyst.com'), **session.cookies.get_dict('.biopharmcatalyst.com')})

    #get site source code
    source_code = requests.get(site_url, headers=headers).text

    #get all pdufa events from the source code
    pdufaEvents = source_code.split('var pdufaEvents = ')[1].split('var pdufaReviewEvents = ')[0]
    pdufaReviewEvents = source_code.split('var pdufaReviewEvents = ')[1].split('var advisoryCommitteeDates = ')[0]
        #advisoryCommitteeDates = source_code[1858].split('= ')[1]

    #parse to json
    pdufaEvents = json.loads(pdufaEvents)
    pdufaReviewEvents = json.loads(pdufaReviewEvents)

    allEvents = pdufaEvents + pdufaReviewEvents

    #get system date to locate next three months data
    start_date = date.today()
    end_date = start_date + timedelta(days)

    #get all entires withing the date range and parse then to print into a csv
    entires_in_date_range = []
    for item in allEvents:
        if start_date <= datetime.strptime(item['date'], '%Y-%m-%d').date() <= end_date:
            entires_in_date_range.append(item)
    return entires_in_date_range
    
#1856 pdufaEvents
#1857 pdufaReviewEvents
#1858 advisoryCommitteeDates