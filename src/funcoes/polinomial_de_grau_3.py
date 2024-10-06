import numpy as np
import matplotlib.pyplot as plt

def funcao_y(x, a, b, c, d):
    return (a * (x**3)) + (b * (x**2)) + (c * x) + d

def funcao_polinomial(a, b, c, d):
    x = np.linspace(-10, 10, 100) 
    y = funcao_y(x, a, b, c, d)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'f(x) = {a}x³ + {b}x² + {c}x + {d}', color='orange')
    plt.title('Gráfico da Função Polinomial de Grau 3')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Linha horizontal em y=0
    plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Linha vertical em x=0
    plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Grade no gráfico
    plt.legend()
    plt.show()
