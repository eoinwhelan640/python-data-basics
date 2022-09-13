import numpy as np

# create a np array by converting a list
mylist = [1,2,3,4]
arr = np.array(mylist)
print(arr)
print(type(arr))

mat = [[1,2,3],[4,5,6],[7,8,9]]
mat_arr = np.array(mat)
print(mat_arr )

# stand in for Python's range function is np.arange()
# Used to generate np arrays
print(np.arange(0,9).reshape((3,3)))

# array of zeros and ones
print(np.zeros(10))
print(np.ones((5,2)))

# np.linspace is used for generating an array of numbers within a certain interval
# not to be confused with np.arange(). The syntax is np.linspace(start,stop,#elements to gen in the range)
print(np.linspace(5,10,5))
# Important to know that the stop & start values are included in generated array, so pick # elements carefully
print(np.linspace(5,10,6))
# THINK about the elements produced, not the number you want
print(np.linspace(0,10,5))


##########
# Start using np.random utils
print(80*'-')
##########
# np.random.rand input is a tuple, dont need the matrix formulation
print(np.random.rand(3))
#print(np.random.rand(3,3))
#print(np.random.rand(3,5))

# Same syntax for std normal distribution
# N(0,1)
np.random.randn(10)
np.random.randn(5,2)

# Generate random integers in a  range
print(np.random.randint(0, 101, (4,5)))

# Setting the seed
# Seed is a way of setting the random library to base it's random generation off a certain starting point
# by setting a seed, results can be reproduced on other machines when people run the script
np.random.seed(42) # hitchhikers guide
np.random.rand(4) # This will be the same everywhere now, random results will be reproducible

##################################################
# Specifically attributes of arrays
##################################################

arr = np.arange(24)
print(arr)

# reshape an array using array.reshape((m, n))
print(f"my array starts as {arr.shape}")
print(f"My 2x12 array - {arr.reshape((2,12))}")
print(f"My 3x8 array - {arr.reshape((3,8))}")
print(f"My 24x1 array - {arr.reshape((24,1))}")


# Max, min and argmax
ranarr = np.random.randint(0, 101, 20)
print(ranarr)
print(ranarr.max())
print(ranarr.min())

# argmax is useful in that it prints the index where the max/min appears
print(ranarr.argmax())
print(ranarr.argmin())

# Find the type of an array, only one type allowed not allowed mix like we can in lists
print(arr.dtype)

# Shape just tells you the shape of the array. Both of these are attributes so no () to invoke
print(arr.shape)

##################################################
# Challenge
##################################################

# TASK: Create a numpy array called myarray which consists of 101 evenly linearly spaced points between 0 and 10.
print(80*'-')
print("Start Challenge")
print(80*'-')
myarray = np.linspace(0,10,101)
# Problem with this one is you need to know the divisible amount, if it was 1/3 you'd have trouble
#myarray = np.arange(0, 10.1, 0.1)
print(myarray)



arr = np.arange(0, 10)
###############################################
print(80*'-')
print('Starting Basic Arithmetic')
print(80*'-')
###############################################
# Basic arithmetic works on arrays just like in array languages like q
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

import numpy as np
account_transactions = np.array([100,-200,300,-400,100,100,-230,450,500,2000])
print(account_transactions)
account_total = account_transactions.sum()
print(f"Account total is {account_total}")
