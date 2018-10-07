import numpy as np
arr = np.arange(10)
print arr

# to save an numpy file we use .npy as an extension
# A new file can created as saved_araay.npy
np.save('saved_array', arr)

# np.load is a function used to reload the array back
new_array = np.load('saved_array.npy')
print "new array"
print new_array

# Save multiple array
array_1 = np.arange(25)
array_2 = np.arange(30)

# savez is used to save a zip file
# npz is a format used for zeze function
np.savez('saved_archieve.npz',x =  array_1,y = array_2)
load_archieve = np.load('saved_archieve.npz')
# this will print out the first array which is array_1
print load_archieve['x']

# saving to a textfile
# to save a txtfile python uses np.savetxtto save to a .txt
np.savetxt('array_text.txt', array_1, delimiter=',')

#to load a txt file it needs a delimiter to separate the array elements
load_txt_file = np.loadtxt('array_text.txt', delimiter=',')
print "load_txt_file is"
print load_txt_file
