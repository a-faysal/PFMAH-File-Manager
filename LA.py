import numpy as np import matplotlib.pyplot as plt
x = input('Enter x values: ').split()
y = input('Enter y values: ').split()
x = [int(i) for i in x]
y = [int(i) for i in y]
meanx = np.mean(x)
meany = np.mean(y)
n = 0
d = 0
for i in range(len(x)):
n += (x[i] - meanx)*(y[i] - meany)
d += (x[i] - meanx)**2
m = n/d
c = meany - (m*meanx)
print('%-s %-.4f %-s %-.4f' % ('B0=',c,'B1=',m))
#plotting the line
maxx = np.max(x) + 100
minx = np.min(x) - 100
xg = np.linspace(minx,maxx,1000)
yg = c + m*xg
plt.plot(xg,yg,label = 'Regression Line')
plt.scatter(x,y,label = 'Scattered points')
plt.legend()
plt.show()