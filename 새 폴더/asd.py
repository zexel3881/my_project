import numpy as np
import matplotlib.pyplot as plt

# Random decimal numbers
print(np.random.rand(4,2))


# step function
def step_function(x):
    y = x > 0
    return y.astype(np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return \
        np.maximum(0, x)


def softmax(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_ = np.sum(exp_x)
    return exp_x / sum_


x = np.arange(-5, 5, 0.05)
y = relu(x)

plt.plot(x, y)
plt.show()


