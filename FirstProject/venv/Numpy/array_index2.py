import numpy as np

# Creating a 2 dimension array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print arr2d
# this prints the index row
print arr2d[0]
# Print a specific element
print arr2d[0][2]

# Slices of 2d array
# the first argument 0:2 looks at the row number and the second argument looks at columns
slice1 = arr2d[0:2, 0:3]
print slice1

# This slice method the first argument looks at from 0 to 2
# and the second argument looks at from 1 to the end of the array
slice2 = arr2d[:2, 1:]
print slice2
# It contains 0 and 1 row index also 1 and 2 column index

# With this code the index 1 and 2 will be changed to 15 for row index 0 and 1 and column index 0 and 1
arr2d[:2, 1:] = 15
print arr2d


print "--------------------------------------"
# Using loops to index
# To use loops in an array you need to know what the size (length)
# of the array is using arr_len = arr2d.shape
# The first number is the number of rows and the second number is the number of columns
# The shape of the arr2d returns two numbers as a list
arr_len = arr2d.shape[0]  # this contains the number of rows in a 2D array


# The loop changes the elements of the array to the same number in each row
for i in range(arr_len):
    arr2d[i] = i;
print arr2d

# Another way of accessing the rows this will print the rows as you
# place the arguments for your array
print arr2d[[1, 1, 2]]

