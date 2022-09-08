import pandas as pd
import numpy as np
import datetime as dt
###############################################
print(80*'-')
print('Starting Formatting data types - strings')
print(80*'-')
###############################################
names = pd.Series(['andrew','bobo','claire','david','4'])

# Our Pandas object can have str methods broadcast across is.
# All the default str methods will work on strings in a pandas series of strings
print(names.str.upper())

# important to know that we need to explicitly invoke the str method, ie str.xyz()
# a pandas series has no method upper/lower/capitalize/isdigit etc, the str method has it
# so this call below wouldn't work, it needs to be names.str.xyz()
#print(names.isdigit()) # Error -> a pd series has no isdigit method
print("5".isdigit()) # True, the 5 is a digit
print(names.str.isdigit()) # broadcast the isdigit str method across the series, checking element wise


# Separating out strings and forming a dataframe
tech_finance = ['GOOG,APPL,AMZN','JPM,BAC,GS']
tickers = pd.Series(tech_finance)

# If we have nested data we can still split it up by invoking st methods
print(tickers)
# str.split again calling str method to broadcast method along series, otherwise would be trying
# to call split() on a pd series which is invalid
print(tickers.str.split(","))
print(tickers.str.split(",")[0]) # Without calling str with the index, we're indexing the pandas object
print(tickers.str.split(",").str[0]) # get first index element wise on the series using str index broadcast

# If we want to turn the separated data into a Dataframe we can use expand=True
# Is good if we had a file where each row was a csv string
#eg Data like  below in a notepad file or something.
# "MSFT, 200, 22, F, 0, 3"
# "GOOG, 100, 44, M, 1, 5"
print(tickers.str.split(",",expand=True))

# We can stack str methods on top of each other to do a lot in one line
messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])
print(messy_names.str.replace(";","").str.strip().str.capitalize())
# could do the same thing with apply if its complicated
# bearing in mind is applying to elements, so is already a string and doesnt need str
def cleanup(name):
    name = name.replace(";","")
    name = name.strip()
    name = name.capitalize()
    return name

messy_names.apply(cleanup)

###############################################
print(80*'-')
print('Starting Timestamps')
print(80*'-')
###############################################
# To illustrate the order of arguments
my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15

# January 2nd, 2017

my_date = dt.datetime(my_year,my_month,my_day)
print(dt.datetime(2017, 1, 2))
# Can get even more granularity
my_date_time = dt.datetime(my_year,my_month,my_day,my_hour,my_minute,my_second)
print(my_date_time)

# Converting a series to a date
myser = pd.Series(['Nov 3, 2000', '2000-01-01', None])

# pd.to_date can be used to convert strings to datetime objects
# Very powerful, can handle multiple formats even within the same series
print(pd.to_datetime(myser))

# If have a problem reading EU vs USA dates, can specify dayfirst to get EU format
print(pd.to_datetime('06-05-2022',dayfirst=True)) # 6th may 22

# Our strings might be stylised in some way, which we can handle with format arg
# format is just a standardised pattern matching system
# %d means 2 digits for day
# %b means 3 letter month code
# %Y means 4 digit year
# -- is how they're separated
pd.to_datetime('12--Dec--2000', format='%d--%b--%Y')


# The process works completely the same with datframes as they're just series objects as well
df = pd.DataFrame({'DATE': ['1992-01-01','1993-02-01','1994-03-01','1994-04-01','1992-05-01'],
                   'MRTSSM4453USN': [1509, 1541, 1597, 1675, 1822]})
print(df['DATE']) # type object
df['DATE'] = pd.to_datetime(df['DATE'])
print(df['DATE']) # type datetime

# We can get the dates parsed when loading a csv with parse_dates arg
#pd.read_csv('path.csv', parse_dates=[0]) # [0] being parse col 0 as dates

# The resample() function is used to groupby time periods
# it is spiritually similar to groupby and does the same thing except only groups by time
# ie df.resample("xyz") creates a resample object similar to lazy groupby
# then we apply some aggregator, eg mean(), to get the DataFrame result
df = df.set_index('DATE') # example of df using resample with date index

df.resample("A").mean() # resample on year basis ("A" is annual) - all the options are in reference
print(df.resample("A").mean())

# Again if you want to access attributes of your date type column, you need to invoke the dt linrary
# exactly the same as we had to do for strings
df = df.reset_index()

# Would fail, a pandas series has no .month attribute, only the individual elements do
#print(df['DATE'].month)
# invoke dt.month to get the individual elemnets when broadcasting across the series
print(df['DATE'].dt.month)





































