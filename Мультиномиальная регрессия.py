import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as sf
import numpy as np

titanic = pd.read_csv('D:/Статистика/Data/GLM/titanik_full_data (1).csv', sep = '\t')
print(titanic.head())

sns.countplot(x = 'Pclass', data = titanic)
plt.xlabel('Класс')
plt.ylabel('Количество')
plt.title('Пассажирские классы')
plt.show()

multi_res = sf.mnlogit('Pclass ~ C(Sex) + Age', titanic).fit()
multi_res.summary()


