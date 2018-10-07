import numpy as np

arr = np.arange(0, 12)
print arr

print arr[0]
print arr[3]
# Print arr[0] will print the array index number

# This will print array form index 0 to index 4 (which is from 0 to 4)
print arr[0:5]
# This is possible by using a colon in between the array index

# With this code the numbers for index 0 to index 4 will be changed to 20
arr[0:5] = 20
print arr

# Interesting thing and important
arr2 = arr[0:6]
print arr2

arr2[:] = 29
# modifies all element
print arr2

# creating new array copy

arrcopy = arr.copy()
