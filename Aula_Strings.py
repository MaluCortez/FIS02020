#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 15:48:14 2025

@author: malucortez
"""

'''
Strings na linguagem python.
Autor: Maria Luísa Cortez
Versão: 0.01 - 13.05.2025
'''

#%% Aspas triplas
docstring = '''
Strings na linguagem python.

Autor: Maria Luísa
Versão 0.01 - 13.05.2025
'''
print(docstring)


#%% escape de caracteres
s = "abc\ndef\nghi"
print(s)

tab1 = "\tabc\t456\t\t789"
tab2 = "123\t456\t789"


print(tab1)
print(tab2)

#%% métodos da classe str
# transformações de maiúscula e minusculas

s = 'abc DEF'
print(s)
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())
#%% 2. Pesquisa e Localização
s = "Linguagem Python"
print(s.find("g"))
print(s.find("g", 4)) #para procurar a partir do 4o caract
print(s.find("x")) #se não tem ele retor "-1"

print(s.rfind("y"))#para enontrar de trás para frente

print()
print(s.index("g"))
#print(s.index("x"))

print(s.count("g"))
print(s.find("gem"))

#%% 3. Verificação boolenas
s = "Linguagem Python"

print(s.startswith("Lin"))
print(s.endswith("Lin "))
print()
print('abc'.isalpha() )
print('1234'.isdigit())
print('12.34'.isdigit())
print('iv'.isdigit())  #testando se são numeros
print()
print('ab1234'.isalnum())
print(' '.isspace())
print('abc'.isupper())     
print('ABC'.isupper())
print()
print('Porto Alegre'.istitle()) 
#%% 4.Remoção de espaços e caracteres

print(' oi '.strip() +"<--")
print(len(' oi '.strip()))

print(' oi '.lstrip() +"<--")
print(' oi '.rstrip() +"<--")

print('-xyz-'.strip('-'))

#%%5. substituiçãp e divisão

print()
x = "123.48"
print(x.replace(".", ","))

s1 = "1,11,23,45"
print(s1.split(","))

s2 = "1 11 23 45"
print(s2.split(' '))
print(s2.split())

s2 = "1, 11, 23, 45"
print(s2.split(', '))

s2 = "1\t11\t23\t45"
print(s2.split('\t'))

#%%6. alinhamento e preenchimento
print()
print("py".center(10, "."))
print("py".ljust(10, "."))
print("py".rjust(10, "."))

print('42'.zfill(5))

#%% exmplos
#1. formatação de coordenadas
ra = 10.684
dec = 41.269
c = f"RA: {ra:6.2f}\u00b0, DEC: {dec:6.2}:\u00b0"

print()
print(c)

"2. interpretação de cabeçalhos"
header = "# ID | RA(deg) | DEC(deg) | Magnitude_V"      
print(header.split("#")[1].replace(" ", "").split("|"))
print(header.lstrip("#").replace(" ", "").split("|"))
#%%
#3. Gerar nome de arquivos
objeto = "M61"
data = "2025-05-13"
banda = "H_alpha"
#teste:
filename = f"{objeto}_{banda}_{data}.fits"
print(filename)
print()
#%%
#codigo para analisar os nomes do sdss
#= sdss+RA+-dec
#filename  = {sdss}{RA}{O}{dec}

obj_name = "sdssJ123456.78+123456.7"
def is_sdss(name):
    if len(name) != 23:   #testando a quant de caract
        return False #caso não seja 
    if not name.startwith('sdssj'): #test se é o sdss
        return False
    if not (name[5:11] + name[12:14] + name[15:21] +
            name[22]).isdigit():   #test tods os numeros
        return False
    if not (name[11] == '.' and name[21] == '.'):
            return False
    if not name[14] in ('=', '-'):
        return False
    return True
print()
print(f'{obj_name} é um arquivo do SDSS')