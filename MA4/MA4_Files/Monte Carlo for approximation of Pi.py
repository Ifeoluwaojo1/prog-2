# Reviewer: 
# Student: Ifeoluwa Ojo

import random
import math
import matplotlib.pyplot as plt

nc = 0
n = 1000
xc = []
yc = []
xs = []
ys = []
for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    c = nc
    if (x**2 + y**2) <= 1:
        c += 1
        xc.append(x)
        yc.append(y)
    else:
        xs.append(x)
        ys.append(y)
    nc = c
print(nc)
print(f'the approximation of pi using Monte Carlo is: {4 * (nc / n)}')
print(f'the real number of pi is: {math.pi}')

plt.xlim(-1, 1)
plt.ylim(-1, 1)    
plt.scatter(xc, yc, color = 'r')
plt.scatter(xs, ys, color = 'b')
plt.show()