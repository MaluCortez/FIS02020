#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:42:19 2025

@author: malucortez
"""

#%% definir uma função python do tipo xy linear (a, b, num de pontos), x1 e x2):
# y = ax +b
#função deve retornar um array com  n linhas e 2 colunas sendo x | y

import numpy as np
import matplotlib.pyplot as plt

def func_grafico(a, b, n, x1, x2, sd):
    x = np.linspace(x1, x2, n)
    sd = 
    error = np.random.normal(0, sd, n)
    y = a * x + b + error
    y2= a * x + b
    print(np.column_stack([x, y]))
    return np.array([x, y])
                          
x, y, y2 = func_grafico(1 , 5, 5, 1,15, )
plt.plot(x,y, y2, '-r', label = '')
plt.plot(x, y, y2, 'ob')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da função y = ax + b')
plt.grid(True)
plt.show()
