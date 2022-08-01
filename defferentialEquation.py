import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ID: 1803510201664(B1) Sayed MD. Sadik Iqbal Akil

def model(y, t):   # function that returns dy/dt
    k = 0.3
    dydt = -k * y
    return dydt


y0 = 5  # initial condition
t = np.linspace(0, 20)  # time points
y = odeint(model, y0, t)  # solve ODE

plt.title("*** #EX-02: Differential_Equation***")
plt.plot(t, y, color="green")
plt.xlabel('time')
plt.ylabel('y(t)')
plt.grid(color="red")
plt.show()
