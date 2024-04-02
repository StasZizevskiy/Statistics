import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as sf
import numpy as np

titanic = pd.read_csv('D:/Статистика/Data/GLM/titanik_full_data (1).csv', sep = '\t')
print(titanic.head())

sns.countplot(x = 'Survived', data = titanic)
plt.xlabel('Выжил ли пассажир')
plt.ylabel('Количество людей')
plt.title('Судьба пассажиров Титаника')

plt.show()

logit_res = sf.glm('Survived ~ C(Pclass) + C(Sex) + Age', titanic, family = sm.families.Binomial()).fit() #буква С перед названием колонки определяет данные как категориальные

logit_res.summary()


