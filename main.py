import bio, yahoo
from baker_bros import get_baker_holdings
#libraries needed to make and open csv files
import csv, os, sys
from platform import system
from datetime import datetime

#progress bar code
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

#establishing the fields in my spreadsheet
fields = ["Ticker", "Date", "Price", "Type", "Drug Name", "Note", "Market Cap",	"Yearly High", "Yearly Low"	,"Target", "Revenue", "Cash", "Debt", "Net Income Avai.", "Baker Bros Own?"]

#gets all entries within 90 days
entries = bio.getEntries(90)

#makes a new line so everything looks cleaner
print("\n")

#rows will eventually hold all data necessary
rows = []
#gets the baker bros info
baker_holdings = get_baker_holdings()
#this iterates through every entry and maps it to the information for that line on the csv
#the first for loop goes through all of the entries but also makes a progeress bar for us
for entry in progressbar(entries, "Fetching: "):
    for i in range(len(entry['companies'])):
        ticker = entry['companies'][i]['ticker']
        yahoo_data = yahoo.scrape(ticker)
        rows.append([ticker, entry['date'], round(entry['companies'][i]["price"], 2), entry['class'], entry['name'], entry['note'], yahoo_data[0], yahoo_data[2], yahoo_data[3], yahoo_data[1], yahoo_data[4], yahoo_data[5], yahoo_data[6], yahoo_data[7], "Yes"  if ticker in baker_holdings else "No"])

#this will create a folder named spreadsheets in teh same folder and it will determine the filname for the csv based on the current date
#this line determines if i am running in a bundle or live and determines the home dir. When doing os.getcwd() on a bundle it gives the hom dir but running sys.executable on a live operation
#   returns the python path
cwd = os.path.dirname(sys.executable) if getattr( sys, 'frozen', False ) else os.getcwd()
os.makedirs(cwd + "/spreadsheets", exist_ok=True)
filename = cwd + "/spreadsheets/curated_list_" + datetime.today().strftime('%Y-%m-%d') + ".csv"

#write to csv file
print("\nWriting to csv file.")
with open(filename, 'w+') as csvfile: 
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows) 

#open csv file
print("\nOpening file now.\n")
platform_name = system()
if platform_name == "Windows" : os.startfile(filename)
elif platform_name == "Darwin": os.system("open {}".format(filename))
elif platform_name == "Linux" : os.system("xdg-open {}".format(filename))
else: print("Your OS is not supported for automatic opening of the CSV file. Please check the current directory for a csv file.")