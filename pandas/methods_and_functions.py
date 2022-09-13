import numpy as np
import pandas as pd

df = pd.read_csv("../csv_data/tips.csv")
###############################################
print(80*'-')
print('Starting Conditional Filtering')
print(80*'-')
###############################################

# Take a given condition - in this case total_bill > 17
# By specifying df['total_bill'] we are getting a Series, which the condition is broadcast across
# it returns a boolean Series object with True where the condition is met
print(df['total_bill'])
print(df['total_bill'] > 17)
#bool_series = df['total_bill'] > 17

# The pd dataframe object allows for indexing based off a boolean series
# So we can pass our generated boolean series into our original dataframe as an index object
# So only rows with a true value for their index are returned
print(df[df['total_bill'] > 17])
print(df[df['sex'] == 'Male'])
# df[bool_series]

# For multiple conditions, it's still a single Boolean series being returned, so functions the same
# when returning rows from original df

# Use & - cannot be "and" from inbuilt python, only symbol works.
# "and" is for atomic cases, not the whole series, ie one value to next
print((df['total_bill'] > 17) & (df['sex']=='Male'))
print(df[(df['total_bill'] > 17) & (df['sex']=='Male')])

# Using | for or operator, same as above cannot be the inbuilt "or" keyword
print((df['total_bill'] > 17) | (df['sex']=='Male'))
print(df[(df['total_bill'] > 17) | (df['sex']=='Male')])


# If we want to check if a categorical column has some value from a selection of values.
# we can use isin() for this

# .isin() is essentially the same as a conditional and is used just the same.
# It broadcasts the check across rows down the column, returning a boolean series like a conditional
#df['day'].isin(['Sat', 'Sun'])
options = ['Sat', 'Sun']
print(df['day'].isin(options)) # check if values of day fall within our stated options, ie the weekend

# We cannot do this for same reason we can't use keywords "and" & "or".
# "in" is meant for checking one value against the specified list, ie checking an atomic value.
# Since we're broadcasting across Series object, it fails
#print(df['day'] in ['Sat', 'Sun'])

# Note if we get error
# ValueError: The truth value of a Series is ambiguous
# we are making the mistake of trying to compare atomic values when broadcasting

###############################################
print(80*'-')
print('Starting Apply()')
print(80*'-')
###############################################
df = pd.read_csv("../csv_data/tips.csv")
# We define our own function which will be applied element wise to the dataframe column we choose.
# input is atomic, it handles single elements not list
def last_four(x):
    return str(x)[-4:]

# Don't need to specify the arg or anything, it knows how to apply it
print(df['CC Number'].apply(last_four))

# We can do the same using a lambda, ie an unsigned function. Same syntax, you're passing in a function
# Just that lambda is unnamed whereas lastfour is a named func
print("Lambda")
print(df['CC Number'].apply(lambda x: str(x)[-4:]))
def yelp_price(amt):
    if amt < 10:
        return "$"
    elif amt < 20:
        return "$$"
    else:
        return "$$$"

df['yelp'] = df['total_bill'].apply(yelp_price)
print(df[['total_bill','yelp']])


# Use apply() with multiple columns
def tip_quality(tip,bill):
    if tip/bill >= 0.2:
        return "Good"
    else:
        return "Bad"

# In this case we pass two columns to the apply function. So the apply is no longer operating on a single Series
# but two Series together, meaning it's a DataFrame object. Can think of apply as working element wise, so before
# each element was atomic value in the column, but now cos two cols are passed, each element is two cells of the df
# Knowing this, when we call tip_quality, we have to index into df object so the right cells are passed to relevant args
# lastly axis=1 is part of apply, telling it to operate down the axes
df['tip_quality'] = df[['tip', 'total_bill']].apply(lambda df: tip_quality(df['tip'], df['total_bill']), axis=1)
print(df['tip_quality'])

# np. vectorize

# Can speed up this massively by using np.vectorize. it achieves the same thing as apply() on multiple cols
# but is more efficient. use np.vetcorize to convert a standard function with atomic inputs so that it works
# on an array. Ie think of kdb+ arrays - apply() by defaults does "func each X", whereas vectorize does "func X"
df['tip_quality_vector'] = np.vectorize(tip_quality)(df['tip'],df['total_bill'])
print(df[['tip_quality','tip_quality_vector']])


###############################################
print(80*'-')
print('Starting Statistical Info, Sorting and Data Methods')
print(80*'-')
###############################################
# brief summary statistics - transpose for easier view
df.describe().transpose()

# Sort data based on a column, default is highest to lowest
# Doesnt sort in place, just displays it
print(df.sort_values('tip'))
print(df.sort_values(['tip','size'], ascending=False)) # Sort by tip then size

# Get index of min and max values
# Very important note here, this is different to argmax. Argmax returns the index the max/min occurs
# wheras idxmax uses to index as specified by Pandas Series/DataFrame index. They may not align
print(df['total_bill'].idxmax())
print(df['total_bill'].idxmin())

# Correlation matrix
print(df.corr())

# value_counts to get unique items in a column and their counts
# Good for categorical data
print(df.value_counts('sex'))

# Get the array of unique values or the number of unique items
print(df['day'].unique()) #returns numpy array
print(df['day'].nunique())

# How to replace data in a dataframe
# Use replace() method
df['sex'].replace('Female','F')
print(df['sex'].replace(['Male','Female'],['M','F'])) # can use list syntax to replace multiple values

# Can also use map() to replace data
# need to first create the dictionary to serve as mapping of one val to another
mymap = {'Male':'M', 'Female':'F'}
df['sex'].map(mymap)

# Find duplicated rows - returns boolean series where True values are first occurences of a duplicate row
df.duplicated()
# Drop duplicated rows, which utilsies ^
df.drop_duplicates()

# between() - use to find where values are between a certain range. Returns boolean series
df['total_bill'].between(10,20, inclusive=True)
# Can be a neat way to index a df since we get a boolean series returned that can be used for indexing
df[df['total_bill'].between(10,20, inclusive=True)]


# Take a random sample from a DataFrame
df.sample(5) # get 5 records
df.sample(frac=0.1) # get sample size of 10% from dataframe














