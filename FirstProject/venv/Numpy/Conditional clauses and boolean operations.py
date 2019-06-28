import numpy as np

x = np.array([100, 400, 500, 600])
y = np.array([10, 15, 20, 25])
condition = np.array([True, True, False, False])

# a loop should be used indirectly to perform this action
z = [a if cond else b for a, cond, b in zip(x, condition, y)]
print z
z2 = np.where(condition, x, y)
print "z2: "
print z2
z3 = np.where(x > 0, 0, 1)
print "z3"
print z3

# Standard functions of numpy
# sum function
print x.sum()
n = np.array([[1, 2], [3, 4]])
# column sum
print x.sum(0)
print n.sum(0)
print x.mean()
print x.std()
print x.var()

# logical operation - and/ or operators
condition2 = np.array([True, False, True])
# any uses an or operator
print condition2.any()
# all uses an and operator
print condition2.all()

# sorting in numpy array
unsorted_array = np.array([1, 5, 2, 9, 3])
print "Unsorted array: "
print unsorted_array
print "Sorted array"
unsorted_array.sort()
print unsorted_array

arr2 = np.array(['solid', 'solid', 'solid', 'liquid', 'liquid', 'gas', 'gas'])
print np.unique(arr2)
# checkers if the variables/ elements are available on the first and second array
print np.in1d(['solid', 'gas', 'liquid'], arr2)
