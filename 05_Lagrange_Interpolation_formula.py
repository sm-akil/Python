# Importing NumPy Library
import numpy as np

# Reading number of unknowns
n = int(input('Enter number of data points: '))

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n))


# Reading data points
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))


# Reading interpolation point
xp = float(input('Enter interpolation point: '))

# Set interpolated value initially to zero
yp = 0

# Implementing Lagrange Interpolation
for i in range(n):
    
    p = 1
    
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    
    yp = yp + p * y[i]    

# Displaying output
print('Final Interpolated value is : %.3f is %.3f.' % (xp, yp))


# Lagrange Interpolation ~ OUTPUT
"""
Enter total number of data points: 3
Enter data for x and y: 
x[0]=0.3333
y[0]=2
x[1]=0.25
y[1]=-1
x[2]=1
y[2]=7
Enter interpolation point: 4
Final Interpolated value is : 4.000 is -388.722.

Process finished with exit code 0
"""
