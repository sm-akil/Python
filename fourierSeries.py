import numpy as np
import matplotlib.pyplot as plt
from math import pi as p

# X(t) = 4/pi (cos pi/2)t -1/3*4/pi cos3(pi/2)t + 1/4*4/pi )(cos5*pi/2)t

t = np.arange(-1, 10, 0.005)
d = 4 / p
s = p / 2
x1 = d * np.cos(s * t)
x2 = (-d / 3) * np.cos(3 * s * t)
x3 = (d / 5) * np.cos(5 * s * t)
fx = 1 + x1 + x2 + x3

plt.plot(t, fx)
plt.xlabel("-Time-", color="red")
plt.ylabel("-Amplitude-", color="red")
plt.title("***Fourier Series***", color="red")

plt.grid(color="yellow")
plt.show()
