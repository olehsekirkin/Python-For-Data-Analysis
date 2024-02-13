import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["figure.dpi"] = 150

from mpl_toolkits.mplot3d import Axes3D
x = np.random.normal(size=100)
y = np.random.normal(size=100)
z = np.random.normal(size=100)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x, y, z, c=np.linalg.norm([x, y, z], axis=0))
plt.show()


ax2 = plt.axes(projection="3d")
x_data = np.arange(-5, 5, 0.1)
y_data = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x_data, y_data)
Z = np.sin(X) * np.cos(Y)
ax2.plot_surface(X, Y, Z, cmap="plasma")
plt.show()

