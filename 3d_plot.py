import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#create a figure
fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.linspace(0, 5, 500)
x = z * np.sin(20 *z)
y = z * np.cos(20 *z)

ax.plot3D(x, y, z)
ax.set_title('3D line plot')
plt.show()