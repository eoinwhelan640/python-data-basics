import pandas as pd
import numpy as np

###############################################
print(80*'-')
print('Starting DataFrames')
print(80*'-')
###############################################
# A Dataframe might look like the below, where Data, POp and GDP all are Series but have common Index
# and thus can be combined as a DataFrame
# Named Index   Data POP GDP
#    USA        1776 328 20.5
#   Canada      1861 38  1.7
#   Mexico      1821 126 1.22

np.random.seed(101)
mydata = np.random.randint(0, 101, (4,3))
print(mydata)

myindex = ["CA", "NY", "AZ", "TX"]
mycolumns = ["JAN", "FEB", "MAR"]

df = pd.DataFrame(mydata, myindex, columns=mycolumns)
print(df)

# Useful way to see some details about the df + it's memory usage
# NOTE - reason df operations are fast is because they're stored in memory
df.info()

###############################################
print(80*'-')
print('Starting Reading from CSV')
print(80*'-')
###############################################
# Lots of different variations on read_*, read _html,_pickle,_json etc
df = pd.read_csv('tips.csv', header=0)
print(df)

# Access the column and index of the df. object returned is an index object
print(df.columns)
print(df.index)
# Must convert to list to get string/ integer list format.
print(list(df.columns))
print(list(df.index))

# Look at first few rows
print(df.head())
# Calculate some basic summary statistics
print(df.describe().transpose()) # use transpose to just make it easier to read sometimes

###############################################
print(80*'-')
print('Starting Working with Columns Index')
print(80*'-')
###############################################

# Access df at column level
print(df['total_bill'])
print(type(df['total_bill'])) # remember is just a series

# Access multiple columns
mycols = ['total_bill', 'tip']
#print(df[['total_bill', 'tip']])
print(df[mycols])

# Arithmetic operations on columns
# syntax is very similar to numpy arrays
print(df['total_bill'] + df['tip'])
print(type(df['total_bill'] + df['tip'])) # returns a Series since it's one row

print(100* df['total_bill'])
print(df['tip'] + 20)
print(df[['total_bill','tip']] + 20)

# Create a new column by assigning output
df['new_col'] = df['total_bill'] + df['tip']
print(df['new_col'])
print(df[['total_bill', 'tip']])

# Remember Series are basically a wrapper around nparrays, so we can apply all the same functions
# from numpy to Series/DataFrames
print(np.round(df['total_bill'] / df['tip'], 3)) # np.round(thing, # decimal places)


# Drop a column from a DataFrame
# .drop() works on both rows and columns. If you have named index you can drop a row via that
# Otherwise specify the column and drop that. axis=0 is row, axis=1 is column

df.drop('new_col', axis=1) # return of .drop() method is the df less the dropped col(s)
#print(df.drop(['total_bill','tip'], axis=1))

# .drop() does not happen in place
# if want to persist the change, you'd need to do
df = df.drop('new_col', axis=1) # this is preferred style by convention
#df.drop('new_col', axis=1, inplace=True)


###############################################
print(80*'-')
print('Starting Utilising Row Index')
print(80*'-')
###############################################

# Specify one of the columns to use as a row index - each index preserving uniqueness
print(df.index)
# set_index() does NOT amend in place, need to reassign
df = df.set_index('Payment ID') # set col as the index, removes it as a listed column
print(df.index)
print(df) # can see we're one less column

# reset our index
df = df.reset_index()
print(df.index)


###############################################
print(80*'-')
print('Starting .iloc() vs .loc()')
print(80*'-')
###############################################
df = df.set_index("Payment ID")

print(df.iloc[0]) # Series object
print(df.iloc[0:3]) # DataFrame object

print(df.loc['Sat3880']) # Series object
print(df.loc[['Sun2959','Sat3880']]) # DataFrame object

# Dropping a row, again use .drop but with axis=0
#df.drop("Sun2959", axis=0)
df = df.drop("Sun2959") # default axis is already 0

# Note - if have a labelled index, cannot use the integer index like iloc.
#df.drop(0, axis=0) # Would error
# Can circumvent this via reassignment while still using numeric index
# df = df.iloc[1:] # cut the first row

# Inserting a new row
one_row = df.iloc[0].copy() # need to take a copy, otherwise one row is a copy of a slice
                            # and throws a warning

one_row['total_bill'] = 1000000

# Use append to insert the row
df.append(one_row)
print(df)