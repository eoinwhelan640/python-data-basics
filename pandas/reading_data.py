import numpy as np
import pandas as pd
import datetime as dt
import csv

###############################################
print(80*'-')
print('Starting Input & Output - CSV')
print(80*'-')
###############################################

# index_col=0 means use the first column in data as our index
df = pd.read_csv("../csv_data/example.csv", index_col=0)
print(df)

# we can write down a csv back to csv format using to_csv
#df.to_csv("file.csv", index=True) # can choose to not write or write the index


###############################################
print(80*'-')
print('Starting Input & Output - HTML')
print(80*'-')
###############################################
import lxml
# If a website has a html format and specifically has the table tags correctly formatted, pandas
# has ability to read those tags. BeautifulSoup is much more dynamic library for anything even slightly
# more complicated
url = 'https://en.wikipedia.org/wiki/World_population'

# Pulls back every table thats on that url using the table tags
df = pd.read_html(url)

#print(df) # can see everything with  a table tag is pulled
print(df[3]) # example of the junk that can be pulled if it has a table tag
print(df[5]) # can even read in a Multilevel index if the table has a header

# similarly can write down a html table
# Can be a neat feature for getting a html table and then editing it locally to jazz it up a bit
# Could upload to own website or something then
mytable = df[4]
#mytable.to_html('mytable.html', index='False')

###############################################
print(80*'-')
print('Starting Input & Output - Excel')
print(80*'-')
###############################################
# We can load in the data froma  workbook with read_excel. We can use sheet_name to specify which sheet
# If there are multiple, the default is sheet_name=None and it reads them all in and creates a dictuionary
# where key is sheet name and value is the actual sheet content as a dataframe
# important to know if any complicated formulas or macros in a sheet, they wont be read in any way
df = pd.read_excel('../csv_data/my_excel_file.xlsx', sheet_name="First_Sheet")
print(df)

# default setting to get dict
df = pd.read_excel('../csv_data/my_excel_file.xlsx')

# if wanted to look at the workbook as an object can read it in like that
wb = pd.ExcelFile('../csv_data/my_excel_file.xlsx')
# With this we can look at some attributes, like the sheet names
print(wb) # a ExcelFile object
print(wb.sheet_names)

# Write down as expected
# Can write down to same workbook creating new sheets, if name one the same it'll overwrite it
df.to_excel("sample.xlsx", sheet_name="One")

# if want to write multiple sheets you need to use ExcelWriter object
with pd.ExcelWriter("sample.xlsx") as writer:
    df.to_excel(writer, sheet_name="two")
    df.to_excel(writer, sheet_name="three")

df2 = pd.ExcelFile("sample.xlsx")
# only get the two, trying to do more than one overwrites it unless using ExcelWriter
print(df2.sheet_names)

###############################################
print(80*'-')
print('Starting Input & Output - SQL Databases')
print(80*'-')
###############################################
# sqlalchemy is used to connect our chsoen SQL databases to the driver
# Lots of availble SQL engines like sqlite, postgres, MySQL etc
from sqlalchemy import create_engine

# Create a temporary sqlite db inside our computers RAM
temp_db = create_engine("sqlite:///:memory:")

# create the stand in db
df = pd.DataFrame(data=np.random.randint(low=0, high=100, size=(4,4)), columns=['A','B','C','D'])
print(df)

# write a df to SQL
# This only works the first time. After a table exists in the memory, we cant write over it with
# this syntax for safety - so it will throw an error on subsequent runs
df.to_sql(name="EOIN", con=temp_db)

# If we want to read in from an sql db, we can take two approaches

# One is to read in the whole table. remember pandas DataFrames are stored in ram so reading in a huge
# table could crash our system - need to be careful
df1 = pd.read_sql(sql="EOIN", con=temp_db, index_col=False) # we dont need the index
print(df1)

# The other way is to run a query on the sql db and read in the resulting table as a DataFrame
df2 = pd.read_sql_query(sql="SELECT A FROM EOIN", con=temp_db) # pass the query in getting only col A
print(df2)






















