# GSVI - Google Search Volume Index. In order to install the plugin you need to enter: "pip install gsvi". Read more: https://pypi.org/project/gsvi/
 

import datetime as dt
import os
import pandas
from gsvi.connection import GoogleConnection
from gsvi.timeseries import SVSeries

# We get the year of the beginning and ending
#!!! We need to pick up this variable through Bot in telegram !!!
gotStartYear = input ("Input start year:")
gotEndYear = input ("Input end year:")
Word = input ("What are you looking for?")
Region = input ("Which region?")

#Converting a value to a number
startYear = int(gotStartYear) 
endYear = int(gotEndYear) 

# series start and end
start = dt.datetime(year=startyear, month=1, day=1)
end = dt.datetime(year=endyear, month=12, day=31)

# make connection to Google Trends and inject connection into the request structure
connection = GoogleConnection()
series = SVSeries.univariate(connection=connection,
                             query={'key': Word, 'geo': Region},
                             start=start, end=end, granularity='MONTH'
                             )
ts = series.get_data()

print(ts)

ts2 = pandas.Series.to_string(ts)

file = open('file.csv', 'w')
file.write(ts2)
file.close()
