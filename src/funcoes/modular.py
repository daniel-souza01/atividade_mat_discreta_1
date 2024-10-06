import numpy as np
import matplotlib.pyplot as plt

def calc_y(x):
    return np.abs(x)

def funcao_modular(x_input):
    x = np.linspace(-10, 10, 100) 
    y = calc_y(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='f(x) = |x|', color='blue')
    plt.scatter(x_input, calc_y(x_input), color='red', label=f'Ponto: ({x_input}, {calc_y(x_input)})', zorder=5)
    plt.title('Gráfico da Função Modular')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')  
    plt.axvline(0, color='black', linewidth=0.5, ls='--')  
    plt.grid(color='gray', linestyle='--', linewidth=0.5)  
    plt.legend()
    plt.show()
