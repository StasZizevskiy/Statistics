import math

d = 4
n = 100

#sd = math.sqrt(d)
sd = 5
x = 10
se = sd/math.sqrt(n)

#i1 = x-2.58*se
#i2 = x+2.58*se
#int99 = [i1, i2]
#print(int99)

i1 = x-1.96*se
i2 = x+1.96*se
int95 = [i1, i2]
print(int95)