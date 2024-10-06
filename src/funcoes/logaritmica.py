import numpy as np
import matplotlib.pyplot as plt

def cal_y(x, a):
    return a * np.log(x)

def funcao_logaritmica(a):
    x = np.linspace(0.1, 10, 100)  
    y = cal_y(x, a)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'f(x) = {a} * log(x)', color='purple')
    plt.title('Gráfico da Função Logarítmica')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')  
    plt.axvline(0, color='black', linewidth=0.5, ls='--') 
    plt.grid(color='gray', linestyle='--', linewidth=0.5) 
    plt.legend()
    plt.show()
