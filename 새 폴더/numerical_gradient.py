import numpy as np


def f1(x):
    return x[0]**2 + x[1]**2


def ddx(f, x):
    h = 0.0001
    a = np.zeros_like(x)

    for idx in range(x.size):
        y = x[idx]

        x[idx] = y + h
        y1 = f(x)

        x[idx] = y - h
        y2 = f(x)

        x[idx] = y
        a[idx] = (y1 - y2) / (2*h)
    return a


def gradient_descent(f, init_x, lr = 0.5, step_num = 100):
    x = init_x
    for i in range(step_num):
        grad = ddx(f, x)
        x -= lr * grad
    return x

print(gradient_descent(f1, np.array([18.0, 7.0])))