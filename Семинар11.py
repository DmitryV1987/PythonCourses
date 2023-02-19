import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    return -12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30

# Корни функции
roots = [fsolve(f, x0)[0] for x0 in np.linspace(-10, 10, 21) if abs(f(fsolve(f, x0)[0])) < 1e-5]
print("Корни функции: ", roots)

# Интервалы, на которых функция возрастает и убывает
df = np.diff(f(np.linspace(-10, 10, 1001))) / 0.1
increasing_intervals = [(i * 0.01 - 10, (i + 1) * 0.01 - 10) for i in range(len(df) - 1) if df[i] > 0]
decreasing_intervals = [(i * 0.01 - 10, (i + 1) * 0.01 - 10) for i in range(len(df) - 1) if df[i] < 0]
print("Интервалы, на которых функция возрастает: ", increasing_intervals)
print("Интервалы, на которых функция убывает: ", decreasing_intervals)

# График функции
x = np.linspace(-10, 10, 1001)
y = f(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции')
plt.grid()
plt.show()

# Вершина функции
df = np.diff(f(x)) / np.diff(x)
vertex = x[np.argmin(df)]
print("Вершина функции: ", vertex, f(vertex))

# Промежутки, на которых f > 0 и f < 0
positive_intervals = [(i * 0.01 - 10, (i + 1) * 0.01 - 10) for i in range(len(y) - 1) if y[i] > 0 and y[i+1] > 0]
negative_intervals = [(i * 0.01 - 10, (i + 1) * 0.01 - 10) for i in range(len(y) - 1) if y[i] < 0 and y[i+1] < 0]
print("Промежутки, на которых f > 0: ", positive_intervals)
print("Промежутки, на которых f < 0: ", negative_intervals)
