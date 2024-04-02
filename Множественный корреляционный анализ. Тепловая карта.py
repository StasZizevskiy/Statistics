import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import seaborn as sns


data = pd.read_csv('D:/Статистика/Data/states.csv')
print(data.head())

sns.heatmap(data.corr(numeric_only=True), annot=True, square=True, cmap='coolwarm')
plt.show()

plt.show()
