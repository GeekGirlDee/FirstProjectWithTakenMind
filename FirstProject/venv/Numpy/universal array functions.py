import numpy as np

# arrange
# square root
# exponential
# random
# addition
# maximum

# reference link for many others

# arrange
A = np.arange(15)
print A

# An arrange method will look at the starting number in this case that is 1 which will be displayed
# the middle number is where the index will stop
# and last number is the addition number for each number or the difference of that number between each number
A =np.arange(1, 12, 2)
print A

# square root
# Sqrt calculates the square root of the arranged arrays
B = np.sqrt(A)
print "B is "
print B

# Exponential
# Calculates the exponential of each element in Arrange A
C = np.exp(A)
print "C is"
print C

# Addition
# It needs two arguments which it will add which can be A and B (A,B)
# or A,C or B,C
D = np.add(A, B)
print "D is "
print D

# Maximum
# Maximum compares two elements from two arrays
E = np.maximum(A,B)
print "E is "
print E

# Additional resources
# scipy.org is a library that needs to be added when working with additional resources
# docs.scipy.org

# Random
F = np.random(A)
print F
