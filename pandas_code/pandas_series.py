import numpy as np
import pandas as pd

###############################################
print(80*'-')
print('Starting pd.Series')
print(80*'-')
###############################################

# Think of a pd Series as a np array but with a named index
# Numeric Index   Named Index   Data
#       0              USA      1776
#       1             Canada    1861
#       2             Mexico    1821

# Create a Pandas series of the above data set
myindex = ['USA', 'Canada', 'Mexico']
mydata = [1776, 1861, 1821]

myseries = pd.Series(data=mydata, index=myindex)
print(myseries)

print(myseries['Mexico'])
print(myseries[0])

###############################################
print(80*'-')
print('Create a series from a dictionary ')
print(80*'-')
###############################################

ages = {'Sam':5, 'Frank':10, 'Spike':7}
print(pd.Series(ages))

###############################################
print(80*'-')
print('Starting Challenge')
print(80*'-')
###############################################
# TASK: Use pandas to grab the expenses paid by Bob.
import pandas as pd
expenses = pd.Series({'Andrew':200,'Bob':150,'Claire':450})

bob_expense = expenses['Bob'] # Use pandas, don't just manually write in the number here.
print(bob_expense)

###############################################
print(80*'-')
print('Starting Series Arithmetic operations')
print(80*'-')
###############################################
# Imaginary Sales Data for 1st and 2nd Quarters for Global Company
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)
print(sales_q1)
print(sales_q2)
# As pd is built off numpy and the Series objects are similar to arrays, arithmetic operations
# broadcast across the whole series
print(sales_q1 * 10)
print(sales_q1 / 100)

# This also works as normal, but beware missing index
print(sales_q1 + sales_q2)

# To get around missing indexes, use the add()/multiply() etc methods for series
print(sales_q1.add(sales_q2, fill_value=0)) #fill_value being the value to replace a missing index with

