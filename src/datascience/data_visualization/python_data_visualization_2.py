# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
a = t**2
b = t**3


# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.plot(t, t, 'r--', t, a, 'bs', t, b, 'g^')
plt.xlabel('Actual Data')
plt.ylabel('Derived Power Data')
sns.set()
plt.show()