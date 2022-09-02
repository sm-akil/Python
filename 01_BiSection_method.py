def func(x):
    return x * x * x * x - x * x + x - 7


def bisection(a, b):
    while func(a) * func(b) >= 0:
        a = 0 + 1
        b = b + 1
    if (func(a) * func(b)) > 0:
        print("Change a and b")
    else:
        c = (a + b) / 2.0
        fc = func(c)
        print("\n \n a \t \t \t b \t \t \t c \t \t \t fc \n \n")
        while abs(fc) > e:
            print(a, "\t", b, "\t", c, "\t", fc, "\n")
            if (func(a) * func(c)) < 0:
                b = c
            else:
                a = c
            c = (a + b) / 2.0
            fc = func(c)
        print("The root is: ", c)


a = float(input("Starting position, a: "))
b = float(input("Ending position, b: "))
e = float(input("Tolerance error, e: "))
bisection(a, b)
