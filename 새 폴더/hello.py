import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_text) = load_mnist(flatten = True, normalize=False)

img = x_train[1].reshape(28, 28)
plt.imshow(img)

print(img)