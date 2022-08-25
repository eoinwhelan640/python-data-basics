import numpy as np

arr = np.arange(0, 10)
###############################################
print(80*'-')
print('Starting Basic Arithmetic')
print(80*'-')
###############################################
# Basic arithmetic works on arrays just like in array loanguages like q
print(arr + 5)
print(arr * 3)
print(arr + arr)

# Important note. Numpy handles division by 0 be creating Nan or inf values
# it outputs a warning but still completes the operation

#print(arr / arr)  # if dividing 0 by 0, you'll get NAN
#print(arr + 1 / arr) # if dividing a number by 0, you'll get inf


###############################################
print(80*'-')
print('Starting Basic Operations in 1D')
print(80*'-')
###############################################

# We can apply mathematical operations to arrays
print(np.sqrt(arr))
print(np.log(1+arr))
print(np.sin(arr)) # no log of 0

# We also have methods to call for regular summary functions
print(arr.mean())
print(arr.var())
print(arr.std())
print(arr.sum())
print(arr.max())

###############################################
print(80*'-')
print('Starting Basic Operations in nD')
print(80*'-')
###############################################
arr2d = np.arange(0, 25). reshape(5,5)
print(arr2d)

arr2d.sum() # uses everything
print(arr2d.sum(axis=0)) # Sum across the rows - meaning travel across row for the sum, ie row 0, row 1, row 2
                        #so youre actually summing the columns when doing this,but its considered moving across rows
print(arr2d.sum(axis=1)) # Sum across the columns




###############################################
print(80*'-')
print('Starting Challenge')
print(80*'-')
###############################################
# TASK: Use numpy to check the total remaining in the account after the series of transactions.
# NOTE: Many different ways to do this!
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/Pierian-Data/225a449484e12e0535fbbac2231b426b

import numpy as np
account_transactions = np.array([100,-200,300,-400,100,100,-230,450,500,2000])
print(account_transactions)
account_total = account_transactions.sum()
print(f"Account total is {account_total}")
