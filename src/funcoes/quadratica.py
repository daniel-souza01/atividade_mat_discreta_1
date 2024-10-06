import numpy as np
import matplotlib.pyplot as plt

def funcao_quadratica(a, b, c):
    def calc_y(x, a, b, c):
        return ((a * (x**2)) + (b * x) + c)

    x = np.linspace(-10, 10, 100)
    y = calc_y(x, a, b, c)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'f(x) = {a}x² + {b}x + {c}', color='green')
    plt.title('Gráfico da Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

