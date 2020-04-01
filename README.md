# Overview

This program scrapes [Biopharmcatalyst's PDUFA calendar](https://www.biopharmcatalyst.com/calendars/pdufa-calendar), this is a calendar for every FDA approval of a drug for public companies. This program will scrap the next three months of PDUFA events, and exports it to a CSV file that we can furthermore filter and sort. After getting these PDUFA events, I build a scraper to scrape [Yahoo Finance](finance.yahoo.com) for other data points about their stock. Finally, I scrape the holdings of the [Baker Brothers](http://www.j3sg.com/Reports/Stock-Insider/Generate-Institution-Portfolio.php?institutionid=4698&DV=yes), a enormous fund that invests in pharmas.

When the program is run a progress bar will appear and when it is finished it will create a folder called "_spreadsheets_" and the **.csv** file will be stored there in the format of `curated_list_YEAR_MONTH_DAY.csv` in numerics.

This program runs in **Python 3.8.2**.

# Installation

The source code here can be compiled to a executable and I have provided these executables on the [releases page](https://github.com/vshah1016/pharma_scraper/releases). You can also just run [main.py](https://github.com/vshah1016/pharma_scraper/blob/master/main.py) if you wish.

## Running the program

Run the following inside of a terminal. After cloning the repository and moving to that directory.

`pip install -r requirements.txt`
\
`python main.py`

## Making the executable

Run the following to generate a executable for your platform, if you do this, you can always just double click the generated executable to run the program.

`pip install -r requirements.txt`
\
`pyinstaller main.py -F -n pharma_scraper -c`
\
**If you are on linux omit the `-c` flag of the last command.**

You will be able to see that a folder called `dist` was created and the executable is inside. If you are unable to run it or it opens a text editor, open a terminal in that directory and run this on macOS and linux: `chmod +x pharma_scraper`. You should be able to run the program now.

## Download

If you do not want to make a executable or run the program or clone anything. You can simply download my pre-made executables for Windows and macOS on the [releases page](https://github.com/vshah1016/pharma_scraper/releases). Unfortunately if you are on linux, you must create the executable yourself.
