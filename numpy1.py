#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:44:40 2025

@author: malucortez
"""

#%% simulando jogo
import numpy as np
#gerar 1000 num aleat. entre 1 e 100
#rand-int = inteiros
aposta = [42, 8, 24, 67, 39]
sorteio = np.random.randint(1, 100, 1000)
print(sorteio)

mask = (sorteio == 42) | (sorteio == 8) | (sorteio == 24) | (sorteio ==67) | (sorteio ==39) 
print(mask)

sorteio[mask] #aqui ele vai mostrar exatamente os numeros que queremos
#%% 
mask = np.isin(sorteio, aposta) 
print(sorteio[mask])


#%%

import numpy as np
import matplotlib.pyplot as plt
a = np.array([1,2,3])
print(a)
print()
b = np.array( [ [1,2], [3,4]])
print(b)



x = np.array( [1,2,3,4,5,6])
print(x)
y = []
x = x/10
print(x)

x = x *np.pi
print(x)

y = np.sin(x)
print(y)

plt.plot(x,y)
plt.show()
