import numpy as np

arr = np.arange(0,11)

###############################################
print(80*'-')
print('Starting simple indexing')
print(80*'-')
###############################################
arr[1]

# Access a slice or range of values
# x:y means index x up to but not including y
arr[1:5]
# also allows us to go from beginning by omitting 0, or to end by omitting end
# This is called broadcasting.
arr[:5] # 0 up to but not including 5
arr[3:] # 3 to the end


# broadcasting one value across others and reassigning.
# Not posisble with in built python list, but numpy allows this
arr[:5] = 100


# Important to know that takening a sub slice of an array does not create a new array
arr = np.arange(0, 11)
slice_of_arr = arr[0:5]
print(arr)
slice_of_arr[:] = 10000
# Our slice variable was not it's own variable, it was a pointer to the original array
print(arr)

###############################################
print(80*'-')
print('Starting 2d indexing')
print(80*'-')
###############################################

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

# Indexing in 2d
arr_2d[1] # gives us row index 1, [20,25,30]
# to get more granular
arr_2d[1][2]
# Instead of directly using the box notation, we can collapse it and separate with commas
arr_2d[1,2] # This also lends to matrix notation, ie m x n matrix, our index at (1,2) is 30. Works for a single matrix
# but will not work for stacked matrices or tensors

# A neat way to broadcast index into N dimensional arrays uses the same syntax as a regular broadcast
arr_2d[:2, 1:] # Get rows to index 2 (0 & 1)and columns from 1 to end (so index 1 & 2). Gives vals [[10,15],[25,30]]

###############################################
print(80*'-')
print('Starting Conditional indexing')
print(80*'-')
###############################################
arr = np.arange(1, 11)
print(f"Array before the conditional - {arr}")
print(arr > 4)
bool_arr = arr>4
print(f"Array after the conditional - {arr[bool_arr]}")

# We can skip the extra syntax here by using the condition directly as an index
print(f"Direct indexing with the conditional is {arr[arr>4]}")


###############################################
print(80*'-')
print('Starting Challenge')
print(80*'-')
###############################################
# TASK: Use numpy to check how many rolls were greater than 2. For example if dice_rolls=[1,2,3] then the answer is 1.
# NOTE: Many different ways to do this! Your final answer should be an integer.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/Pierian-Data/ea3121efac5dd3338c280ff10068f9c8

dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

total_rolls_over_two = len(dice_rolls[dice_rolls > 2])# This should be a single integer
print(total_rolls_over_two)
