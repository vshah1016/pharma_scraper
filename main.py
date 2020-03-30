import bio
import yahoo
#libraries needed to make and open csv files
import csv, platform, os
from datetime import datetime

#establishing the fields in my spreadsheet
fields = ["Ticker", "Date", "Price", "Type", "Drug Name", "Note", "Market Cap",	"Yearly High", "Yearly Low"	,"Target", "Revenue", "Cash", "Debt", "Net Income Avai.",]

entries = bio.getEntries(90)

#this iterates through every entry and maps it to the information for that line on the csv
#keeping a count for progress bar
rows = []
count = 0
entries_len = len(entries)
for entry in entries:
    for i in range(len(entry['companies'])):
        ticker = entry['companies'][i]['ticker']
        yahoo_data = yahoo.scrape(ticker)
        rows.append([ticker, entry['date'], round(entry['companies'][i]["price"], 2), entry['class'], entry['name'], entry['note'], yahoo_data[0], yahoo_data[2], yahoo_data[3], yahoo_data[1], yahoo_data[4], yahoo_data[5], yahoo_data[6], yahoo_data[7], ])
    count += 1
    print('Fetched data {}/{} done.'.format(count, entries_len))

#write to csv file
filename = "curated_list_" + datetime.today().strftime('%Y-%m-%d') + ".csv"

print("\nwriting to csv file")
with open(filename, 'w+') as csvfile: 
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows) 

#open csv file
print("\nopening file now")
platform_name = platform.system()
if platform_name == "Windows" : os.startfile(filename)
elif platform_name == "Darwin": os.system("open {}".format(filename))
elif platform_name == "Linux" : os.system("xdg-open {}".format(filename))
else: print("Your OS is not supported for automatic opening of the CSV file. Please check the current directory for a csv file.")