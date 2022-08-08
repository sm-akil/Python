import numpy as np
import matplotlib.pyplot as plt
from math import pi as p

t = np.arange(-1, 10,0.005)
k = 4/p
# ID: 1803510201664(B1) Sayed MD. Sadik Iqbal Akil
#print(k)
m = p/2
#print(m)
a1 = k*np.cos(m*t)
a2 = (-k/3)*np.cos(3*m*t)
a3 = (k/5)*np.cos(5*m*t)
a4 = (-k/7)*np.cos(7*m*t)
a5 = (k/9)*np.cos(9*m*t)

x = 1 + a1 + a2 + a3 + a4 + a5

plt.plot(t,x, color="red")
plt.xlabel("Time", color ="blue")
plt.ylabel("Amplitute", color="blue")
plt.title("Fourier Series of Periodic Signal")
plt.grid(color="green")
plt.show()