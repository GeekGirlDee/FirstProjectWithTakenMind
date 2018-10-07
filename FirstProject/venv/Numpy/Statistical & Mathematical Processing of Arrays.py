import numpy as np
import matplotlib.pyplot as plt

# it ranges from - 100 to 100 then 10 it is an array
axes_values = np.arange(-100, 100, 10)

# meshgrid groups the points with every other points
# It maps variables
dx, dy =np.meshgrid(axes_values, axes_values)

print "dx: "
print dx

print "dy: "
print dy

# This function will display 2 times the value of dx and 3 times the value of dy
function = 2*dx+3*dy
function2 = np.cos(dx) + np.cos(dy)

print function
# print function2

#imshow is a function of plt which is used to plot a graph or a chart
# plt.imshow(function)
# plt.title("funtion of plot 2*dx+3*dy")
# colorbar explains what the color means to the user
# plt.colorbar()
# plt.savefig('myfig.png')

plt.imshow(function2)
plt.title("funtion of cos plot")
# colorbar explains what the color means to the user
plt.colorbar()
plt.savefig('myfig2.png')
