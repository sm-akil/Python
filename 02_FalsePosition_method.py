def func(x):
    return x * x * x * x - x * x + x - 7


def falsi(a, b):
    while func(a) * func(b) >= 0:
        a = 0 + 1
        b = b + 1
    if (func(a) * func(b)) > 0:
        print("Change a and b")
    else:
        c = ((b * func(a)) - (a * func(b))) / (func(a) - func(b))
        fc = func(c)
        print("\n \n a \t \t \t b \t \t \t c \t \t \t fc \n \n")
        while abs(fc) > e:
            print(a, "\t", b, "\t", c, "\t", fc, "\n")
            if (func(a) * func(c)) < 0:

                b = c
                fb = fc
            else:
                a = c
                fa = fc
            c = ((b * func(a)) - (a * func(b))) / (func(a) - func(b))
            fc = func(c)
        print("The root is: ", c)


a = float(input("Starting position, a: "))
b = float(input("Ending position, b: "))
e = float(input("Tolerance error, e: "))
falsi(a, b)
