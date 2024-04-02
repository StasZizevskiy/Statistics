import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data = pd.Series([1, 2, 3, 4, 5, 6])
#
## find quartile values
#print(data.quantile([0.25, 0.5, 0.75]))



# create a dataframe
data = pd.DataFrame({'Name': ['Akhil', 'Nikhil', 'Satyam', 'Sravan', 'Pavan'],
                     'Marks': [77, 95, 89, 78, 64],
                     'Credits': [8, 10, 9, 8, 7]})

# box plot
data['Marks'].plot(kind='box', title='Marks of students')
plt.show()