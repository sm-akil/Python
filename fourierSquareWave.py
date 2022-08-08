import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import square

# ID: 1803510201664(B1) Sayed MD. Sadik Iqbal Akil

L=1
x=np.arange(-L,L,0.001)

y=square(2*np.pi*x)

plt.plot(x,y,'r--', color="red")
plt.title("Fourier series for Periodic square wave", color="green")
plt.show()