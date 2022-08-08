from scipy import signal
import matplotlib.pyplot as plot
import numpy as np

t = np.linspace(-1, 1, 10, endpoint=True)

# Plot the square wave
plot.plot(t, signal.square(1 * np.pi * 5 * t))

# Give x,y,title axis label
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('Square wave')

plot.axhline(y=0, color='red')

# Display
plot.show()
