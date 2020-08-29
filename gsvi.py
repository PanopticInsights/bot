# GSVI - Google Search Volume Index. In order to install the plugin you need to enter: "pip install gsvi". Read more: https://pypi.org/project/gsvi/
 

import datetime as dt
import os
import pandas
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
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
start = dt.datetime(year=startYear, month=1, day=1)
end = dt.datetime(year=endYear, month=12, day=31)

# make connection to Google Trends and inject connection into the request structure
connection = GoogleConnection()
series = SVSeries.univariate(connection=connection,
                             query={'key': Word, 'geo': Region},
                             start=start, end=end, granularity='MONTH'
                             )
googleData = series.get_data()

titleGraph = print ("Your results from " + gotStartYear + " to " + gotEndYear + " is:")

#googleDataStr = pandas.Series.to_string(googleData)

#file = open('file.csv', 'w')
#file.write(googleDataStr)
#file.close()

plt.plot(googleData)

plt.savefig('file.png')

#['file.csv'].plot()
