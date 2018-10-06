import numpy as np

# one dimension array
# my_list = {1, 2, 3, 4}
# my_array1 = np.array(my_list)
# print my_array1

# In python when declaring or making statements a space between variables
# is required to avoid white or yellow underlines

#
# print np.array([2,4])

# two dimension array
my_list1 = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8]

my_array = np.array([my_list1, my_list2])
print my_array

# using Shape function
# This will show number of rows(2) and columns(4)
print my_array.shape

# Funding out the data-types of the members of the array
print my_array.dtype

# zero, ones, empty, eye, arrange

# new_array = np.zeros(5)  # creates a new numpy array with 1*5. All elements are zero
# print new_array

new_array_empty = np.empty(5)  # creates a new numpy array with [5.97501354e-294 5.97494187e-294
# 5.97487019e-294 5.97479852e-294 5.97472684e-294
print new_array_empty

new_array_eye = np.eye(5)  # creates a new numpy array with 1*5. All elements are zero
print new_array_eye


# np.delete(remove new_array_arange,5)
new_array_arranges = np.arange(5, 50, 4)  # creates a new numpy array which adds 5 after every last number till it gets to 50
print new_array_arranges

