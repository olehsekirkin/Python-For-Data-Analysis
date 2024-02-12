import seaborn as sns
import matplotlib.pyplot as plt
import numpy

sns.get_dataset_names()

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
planets = sns.load_dataset("planets")

# Simple plots

sns.scatterplot(x="tip", y="total_bill", data=tips, hue="day", size="size", palette="YlGnBu")
plt.show()

sns.histplot(tips["tip"], kde=True,bins=15)
plt.show()

sns.distplot(tips["tip"], kde=True, bins=15)
plt.show()

sns.barplot(x="sex", y="tip", data=tips, palette="YlGnBu")
plt.show()

sns.boxplot(x="day", y="tip", data=tips, hue="sex", palette="YlGnBu")
plt.show()

sns.stripplot(x="day", y="tip", data=tips, hue="sex", palette="YlGnBu", dodge=True)
plt.show()

# More complicated. Joint plots

sns.jointplot(x="tip", y="total_bill", data=tips, kind="reg")
plt.show()

sns.jointplot(x="tip", y="total_bill", data=tips, kind="kde", shade=True, cmap="YlGnBu")
plt.show()

sns.jointplot(x="tip", y="total_bill", data=tips, kind="hex", cmap="YlGnBu")
plt.show()

# Pair plot

sns.pairplot(titanic.select_dtypes(['number']), hue="pclass")
plt.show()

# Heat map

numeric_columns_titanic = titanic.select_dtypes(include='number')
sns.heatmap(numeric_columns_titanic.corr(), annot=True, cmap="YlGnBu")
plt.show()


