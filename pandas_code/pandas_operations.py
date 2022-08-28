import numpy as np
import pandas as pd
df = pd.read_csv("tips.csv")
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


