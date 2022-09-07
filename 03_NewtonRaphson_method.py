# Defining Function
# import numpy as np


def f(x):
    return x ** 4 - x ** 3 + x - 7


# Defining derivative of function
def g(x):
    return 4 * x ** 3 - 3 * x ** 2 + 1


# np = 4 * x ** 3 - 3 * x ** 2 + 1
# return np.diff(f(x))


# Implementing Newton Raphson Method

def newtonRaphson(x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = input('Enter initial guess : ')
e = input('Tolerable Error : ')
N = input('Enter maximum number of steps : ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)

# Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method

newtonRaphson(x0, e, N)

"""
Enter initial guess : 1
Tolerable Error : 0.0001
Enter maximum number of steps : 20
"""
