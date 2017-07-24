import graphics2 as graphics
import numpy as np

N = 10000000
x = np.random.normal(4, 2, N)
y = np.random.normal(3, 1, N)
graphics.plotAsteroids(x,y)
