import scipy.stats as st

point = 150
mean = 150
std = 8

z = (point - mean) / std

if point > mean:
    probability_of_point = (1 - st.norm.cdf(z))
else:
    probability_of_point = (st.norm.cdf(z))

print(f'{round(probability_of_point*100, 2)}%') #округление до второго знака