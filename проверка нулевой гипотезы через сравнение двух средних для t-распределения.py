import scipy.stats as st
import math
import numpy as np

x_1 = 45
sd_1 = 9

x_2 = 34
sd_2 = 10

n1 = 100
n2 = 100
alpha = 0.95

se = math.sqrt(sd_1**2 / n1 + sd_2**2 / n2)
t = (x_1 - x_2) / se

df = n1 + n2 - 2

p_value = np.abs(st.t.ppf((1 - alpha) / 2, df))

print(f"""t-value: {t}
p-value for the {alpha * 100}% confidence interval: {p_value}
""")
if t > p_value:
    print("t > p_value --> rejecting the null hypothesis")
elif t < p_value:
    print("t < p_value --> accepting the null hypothesis")