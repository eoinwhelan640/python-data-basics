import numpy as np
import pandas as pd

df = pd.DataFrame( {'first_name': {0: 'Tom', 1: float('nan'), 2: 'Hugh', 3: 'Oprah', 4: 'Emma'}, 'last_name': {0: 'Hanks', 1: float('nan'), 2: 'Jackman', 3: 'Winfrey', 4: 'Stone'}, 'age': {0: 63.0, 1: float('nan'), 2: 51.0, 3: 66.0, 4: 31.0}, 'sex': {0: 'm', 1: float('nan'), 2: 'm', 3: 'f', 4: 'f'}, 'pre_movie_score': {0: 8.0, 1: float('nan'), 2: float('nan'), 3: 6.0, 4: 7.0}, 'post_movie_score': {0: 10.0, 1: float('nan'), 2: float('nan'), 3: 8.0, 4: 9.0}} )
###############################################
print(80*'-')
print('Starting Missing Data')
print(80*'-')
###############################################
print(df.head())

# detect nulls
df.isnull() # returns boolean true false matrix with nulls being true
df.notnull() #opposite matrix to ^

# You can utilise the boolean output by looking at one col and using it for indexing into the df
have_prescore = df[df['pre_movie_score'].notnull()]

print(have_prescore)

# combining the null with another condition
print(df[(df['pre_movie_score'].notnull()) & (df['sex'] =='f')])
print(df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())])


# Dropping the NA values
df.dropna() # drop any rows with NA values
df.dropna(axis=1) # drop any columns with NA vals. Note this is too powerful, any NA value means the whole
                    # column would get deleted - dont really use this
df.dropna(thresh=3) # drop rows with NA unless they have at least 3 normal values.
df.dropna(subset=['first_name','pre_movie_score']) # drop rows with NAs in the cols firstname & premoviescore

# Filling missing values - use .fillna()
df.fillna(0) # fill nulls with 0
df.fillna("XYZ") # fill nuls with string xyz. fill na will let us use anything, it wont check datatype

df['post_movie_score'].fillna(10) # fill a column
df['post_movie_score'] = df['post_movie_score'].fillna(10) # reassign an amended column

# We can utilise a function like the mean to fill in values
df['pre_movie_score'].fillna(df['pre_movie_score'].mean())

# A kind of quick and dirty way to do this is
#df.fillna(df.mean()) # likely to be deprecated- fills means by col ignoring any categorical type columns


# Filling with interpolation
airline_tix = {'first':100,'business':np.nan,'economy-plus':50,'economy':30}
print(airline_tix)
ser = pd.Series(airline_tix)

# requires the data sorted in either ascending or descending order
# takes an average between the missing values to fill it in
ser.interpolate()


###############################################
print(80*'-')
print('Starting Groupby operations')
print(80*'-')
###############################################
df = pd.read_csv('../csv_data/mpg.csv')

print(df.head())
print(df['model_year'].unique()) # check our likely categorical col
print(df['model_year'].value_counts()) # similar

# Group by lets us use columns to create groupings we can apply aggregate functions to
# for example, group by sex and city to find max val etc
# similar functionality to kdb+ select..by..., apply aggregate func to get atomic values
gb_object = df.groupby('model_year')

# Doing just the groupby creates a "lazy" groupby object, ie it's not done anything yet
# similar to a generator, it's just waiting for the aggregation
print(gb_object)

# create the completed grouping with aggregate function
# result is a DataFrame with the chosen grouping acting as index.
#Only columns with valid data type for the aggregation is returned,ie cat columns will mostly be excluded
print(gb_object.mean())
gb_object.count()

# The aggregation func does not have to create a single atomic result like mean/max etc do
# for example .describe() will create the summary statistics within category per column
print(df.groupby('model_year').describe()) # Again, is still a DataFrame and can be accessed as normal
#print(df.groupby('model_year').describe().transpose())


# can index into this dataframe as normal, treated exact same as df
df.groupby('model_year').mean()['mpg']
print(df.groupby('model_year').mean().loc[80]) # still iuse indexing as normal

# We can also index by two columns
# This creates a dataframe that has a multi index. In this case two levels
print(df.groupby(['model_year', 'cylinders']).mean())
print(f"The columns are {df.groupby(['model_year', 'cylinders']).mean().columns}")
#print(f"The index is {df.groupby(['model_year', 'cylinders']).mean().index}")

# Even with multiple groupings, the output is still just a DataFrame, albeit with a multilevel index
# we can still access as usual
print("-------------Index using loc---------------")
year_cyl = df.groupby(['model_year', 'cylinders']).mean()
print(year_cyl['mpg']) # access columns as normal
print(year_cyl.loc[70]) # index starts from outside in
print(year_cyl.loc[[70,80]]) # use list syntax for 1+ vals from first index
print(year_cyl.loc[70,6])#the index is a tuple to use both indexes
# To take multiple single line snippets, wrap the tuples into a list
print(year_cyl.loc[[(70,6),(80,4)]])

# To take a cross section of multiple rows, ie get all values within a category
# you must use the cross section method .xs()
print(year_cyl.xs(key=70, level ='model_year')) # every value of cylinder for model year = 70
print(year_cyl.xs(key=6, level ='cylinders')) # every value of model year where cylinder = 6

# Can swap the multi level indexes around
year_cyl.swaplevel()
# can also sort it - best to sort from outside level in, can do asc/desc order
year_cyl.sort_index(level="model_year", ascending=False)

# We can apply multiple aggregations using .agg() method- a generalised grouping & aggregation method
# It allows for multiple cols to have aggregation funcs applied
# including allowing different aggregations on different columns
# The aggregation funcs must come from list of valid aggregations per documentation
print(df.agg(['std','mean'])) # apply std and mean to all cols, ignores categorical cols

# the result is a df, so can index and columns we want, eg mean of "year" or cat variable not relevant
df.agg(['std','mean'])

# Best feature is the ability to apply the function to different cols and even apply different
# aggregators to cols. Can specify what we want to do using the dictionary syntax input
aggs = {'mpg':['max','mean'], 'weight':['mean','std']}
aggs_2 = {'mpg':['mean'], 'weight':['mean','std']}
print(df.agg(aggs))
print(df.agg(aggs_2))


###############################################
print(80*'-')
print('Starting Combining DataFrames with concat')
print(80*'-')
###############################################
one = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3']})
two = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']})
print(one)
print(two)

# combine the two along the columns, ie join them side by side, provided the indexes match
print(pd.concat([one,two],axis=1))

# If want to join them length wise, or on top of each other, you need cols to be same.
# if have a named index, the name should match
two.columns = one.columns # rename the columns aby amending the columns attribute
pd.concat([one,two])#could say axis=0 but its the default so no need

# Note - when you merge end to end like this, if the indexes are unamed they wont update automatically
# You'll need to reassign them
merged_df = pd.concat([one,two])
print("INDEX BEFORE")
print(merged_df)
merged_df.index = range(len(merged_df))
print("INDEX AFTER")
print(merged_df)




###############################################
print(80*'-')
print('Starting Combining DataFrames with .merge()')
print(80*'-')
###############################################
registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})

# Doing an inner join, so the intersection or whats common to both only
print(pd.merge(registrations, logins, on='name', how='inner')) # order of df in arg not important

# With left and right merging, it treats one side as master table and brings over the matching data
# from the other table. the
print(pd.merge(registrations, logins, on='name', how='left'))
print(pd.merge(left=registrations, right=logins, on='name', how='right')) # cos order matters it's helpful to
                                                               # specify left and right tables
#pd.merge(logins,registrations, on='name', how='right')#would be the same as left merge

# The outer merge just adds everything together, so basically A U B or union
pd.merge(registrations, logins, on='name', how='outer') # order not important

# We can join where one df has an index and the other a matching col, and vice versa
registrations = registrations.set_index('name')
print(pd.merge(registrations, logins, left_index=True, right_on='name'))

# we can also merge on separate col names when we know they have matching data
registrations = registrations.reset_index()
registrations.columns = ['reg_name','reg_id']
# different col names but the merge still works ok
print(pd.merge(registrations, logins, how ="inner",left_on="reg_name", right_on='name'))

# If we have tables with exact same names but different data in places, or even same data
# (if same you should know to concat not merge)
# when you merge them, pandas recognises duplicates and creates new cols automatically
registrations.columns = ['name','id']
logins.columns = ['id','name']
pd.merge(registrations,logins,on='name')
# can specify our own renaming convention
pd.merge(registrations,logins,on='name',suffixes=('_reg','_log'))



###############################################
print(80*'-')
print('Starting Input & Output - pivot tables')
print(80*'-')
###############################################

# We have two methods for pivoting tables
# pivot() pivots the data to be represented how we want
# pivot_table() also pivots the table but allows an additional aggregation function to be applied
# pivot is purely for descriptive / aesthetic purposes, ask can a group by or some other operation
# achieve the same thing

sales = pd.read_csv("../csv_data/Sales_Funnel_CRM.csv")

licenses = sales[['Company','Product','Licenses']]

# pivot function to recategorise the license values by company and product
# index is what will become the index on Y axis. SHould be limited set of repating values
# columns is the column name that will have its values converted into column names on top x axis
                                           # should again be categorical limited range of values
# values is the column we're trying to represent and will be whats in the actual cells of the df
p_df = pd.pivot(data=licenses, index='Company', columns="Product", values="Licenses")
print(p_df) # NANs are where no values exits for that

# Using pivot_table lets us apply an aggregation function
pd.pivot_table(data=sales, index="Company", aggfunc="sum")

# in cases where columns don't make sense to apply an aggregation, can specify values for cols we want
# and create a multi level index as well, it's very flexible and we can go quite deep
print("----------------------------------")
piv = pd.pivot_table(data=sales, index=["Account Manager","Contact"], aggfunc="sum", values=["Sale Price"])
print(piv)

print("----------------------------------")
# Optionally add in the columns too, getting sale price separated out by product
# essentially two tiers of multi level indexing - two tiers for index and two tiers for columns
# also add fill_value arg for filling nulls with whatever value we want
piv2 = pd.pivot_table(data=sales,
                     index=["Account Manager","Contact"],
                     aggfunc="sum",
                     columns=["Product"],
                      fill_value=0,
                     values=["Sale Price"])
print(piv2)


print("----------------------------------")
# Lastly we can even add in multiple funcs to apply as aggregates, ie pass in a list
# The funcs do not have to be a string, they can be explcit func calls, once they work as a broadcast
# and are an aggreggator
# very complex structure - looks well in jupyter
# margins = True at the end gives you a nice kinda summary printout of totals
piv3 = pd.pivot_table(data=sales,
                      index=["Account Manager","Contact"],
                      aggfunc=["sum",np.mean],
                      columns=["Product"],
                      fill_value=0,
                      values=["Sale Price"],
                      margins=True)
print(piv3)

# Again, pivots and groupby are very similar and can do very similar things
