import numpy as np 
import matplotlib.pyplot as plt 
#create data points
x = np.linspace(-10, 10, 100)
y = np.linspace(-15, 15, 100)
#create grid
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)
fig = plt.figure(figsize=((9,6)))
ax = plt.axes(projection = '3d')
print(ax)
