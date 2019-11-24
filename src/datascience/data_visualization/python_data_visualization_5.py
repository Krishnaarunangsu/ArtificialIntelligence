import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

x = list([1, 2, 3, 4])
y = list([1, 4, 9, 16])
# y = list([1, 4, 9, 'a'])
plt.plot(x, y, 'ro')
# plt.plot('x'= x, 'y' = y, 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
