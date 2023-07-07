import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return x**3


def f2(x):
    return np.exp(x)


def derivative(f, x):
    h = 1e-4
    return (f(x+h) - f(x)) / h


def derivative2(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)


def derivative3(f, x):
    h = 1e-4
    return (f(x) - f(x-h)) / h


x = np.arange(-3, 3, 0.01)

y1 = derivative(f1, x)
y2 = derivative2(f1, x)
y3 = derivative3(f1, x)

z1 = derivative(f2, x)
z2 = derivative2(f2, x)
z3 = derivative3(f2, x)


print(np.sum(y1 - 3*x**2))
print(np.sum(y2 - 3*x**2))
print(np.sum(y3 - 3*x**2))
print()
print(np.sum(z1 - f2(x)))
print(np.sum(z2 - f2(x)))
print(np.sum(z3 - f2(x)))


