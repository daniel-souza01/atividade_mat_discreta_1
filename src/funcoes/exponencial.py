import numpy as np
import matplotlib.pyplot as plt

def cal_y(x, a, b):
    return a * np.exp(b * x)

def funcao_exponencial(a, b):
    x = np.linspace(-10, 10, 100)  
    y = cal_y(x, a, b)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'f(x) = {a}e^({b}x)', color='green')
    plt.title('Gráfico da Função Exponencial')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--') 
    plt.axvline(0, color='black', linewidth=0.5, ls='--') 
    plt.grid(color='gray', linestyle='--', linewidth=0.5) 
    plt.legend()
    plt.show()
