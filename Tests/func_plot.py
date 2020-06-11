import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return np.sqrt((10 ** 10) / ((10 ** 4 - 4 * np.pi ** 2 * x ** 2) ** 2 + 4 * np.pi ** 2 * x ** 2))


x = np.linspace(1, 10**1.72, 10**2)
y = func(x)
print(len(x))

plt.loglog(x, y, 'g')
plt.title("Модуль передаточной функции")
plt.tight_layout()
plt.grid()
plt.show()
plt.savefig()
