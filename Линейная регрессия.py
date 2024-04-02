import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

df = pd.read_csv('D:/Статистика/Data/states.csv')
print(df.head())

# metro_res - процент населения живущие в столице
# white - процент белого населения
# hs_grad - процент людей со образованием
# poverty - уровень бедности
# female_house - процент домов, где есть домохозяйки

sns.jointplot(x='hs_grad', y='poverty', data=df, kind='reg', color='m')
plt.show()

df_descr = df.describe().transpose()
print(df_descr)

slope, intercept, r, p, std_err = linregress(df['hs_grad'], df['poverty'])

x = np.linspace(75, 100)

reg = lambda x: intercept + slope * x
plt.scatter(x='hs_grad', y='poverty', data=df, label='data')
plt.xlabel('hs_grad %')
plt.ylabel('poverty %')
plt.title('Linear Regression')
plt.plot(x, reg(x), color='r', label='fitted line')
plt.legend()
plt.show()
