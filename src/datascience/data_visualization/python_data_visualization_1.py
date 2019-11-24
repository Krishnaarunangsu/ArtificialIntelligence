# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
# x = np.linspace(0, 10, 100)
x = np.linspace(start=0, stop=10, num=20)
print(x)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()

# Reference :
# 1) https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
