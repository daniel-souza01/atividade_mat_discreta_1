import matplotlib.pyplot as plt
import numpy as np

def funcao_linear(a, b):
    def cal_x(x, a, b):
        return a * x + b

    x = np.linspace(0, 10)
    y = cal_x(x, a, b)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'f(x) = {a}x + {b}', color='orange')
    plt.title('Gráfico da Função Linear')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()
