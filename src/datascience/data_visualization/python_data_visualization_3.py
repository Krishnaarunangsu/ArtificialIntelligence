import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
tips = sns.load_dataset("tips")
ax = sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

ax = sns.scatterplot(x="total_bill", y="tip", hue="time",
                     data=tips)
plt.show()

ax = sns.scatterplot(x="total_bill", y="tip",
                     hue="time", style="time", data=tips)
plt.show()


# https://seaborn.pydata.org/generated/seaborn.scatterplot.html
