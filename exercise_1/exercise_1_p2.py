import matplotlib.pyplot as plt
import numpy as np

#a)
P = np.linspace(0, 1, 11)

#b)


def L_1(x, P):
    return ((x - P[0]) * (x - P[2])) / ((P[1] - P[0]) * (P[1] - P[2]))

P_test = np.array([1, 2, 3])
x_values = np.linspace(0.5, 3.5, 50)
L_1_values = L_1(x_values, P_test)

#c)
plt.plot(x_values, L_1_values, label=r'$L_{1}(x)$', color='blue')
plt.title(r'$L_{1}(x)$ vs x')
plt.xlabel(r'$x$')
plt.ylabel(r'$L_{1}(x)$')
plt.legend()
plt.grid(True)

#d)

def L_0(x, P):
    return ((x - P[1]) * (x - P[2])) / ((P[0] - P[1]) * (P[0] - P[2]))

def L_2(x, P):
    return ((x - P[0]) * (x - P[1])) / ((P[2] - P[0]) * (P[2] - P[1]))

L_0_values = L_0(x_values, P_test)
L_2_values = L_2(x_values, P_test)

plt.plot(x_values, L_0_values, label=r'$L_{0}(x)$', color='red')
plt.plot(x_values, L_2_values, label=r'$L_{2}(x)$', color='green')

plt.legend()
plt.show()

