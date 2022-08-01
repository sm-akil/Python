from scipy import signal
import matplotlib.pyplot as plot
import numpy as np

t = np.linspace(0, 1, 1000, endpoint=True)

# Plot the square wave
plot.plot(t, signal.square(2 * np.pi * 5 * t))

# Give x,y,title axis label
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('Square wave - Geeksforgeeks')

plot.axhline(y=0, color='k')

# Display
plot.show()
