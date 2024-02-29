#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys 
import time
print("===== Iterador =====")
lista = [2,6,7,8]

print(type(lista))

print(hasattr(lista, "__iter__"))

for item in lista:
    print(item)

print("======= Iterável =======")    

lista_iteravel = iter(lista)
print(hasattr(lista_iteravel, "__next__"))      
print(type(lista_iteravel))
print(next(lista_iteravel))
print(next(lista_iteravel))
print(next(lista_iteravel))
print(next(lista_iteravel))


print("====== Processando ======")
def gera_lista_dados():
    lista = []
    for n in range(51):
        lista.append(n)
        time.sleep(0.2)
    return lista

numeros = gera_lista_dados()
for item in numeros:
    print(item)

print("======= Fim da ação ======")
time.sleep(3)
os.system("clear")

print("====== Não segura o processamento =======")
def gera_lista():
    for  n in range(51):
        yield n
        time.sleep(0.2)

numeros = gera_lista()
print(next(numeros))
print(next(numeros))
print(next(numeros))
for item in numeros:
    print(item)

lista_c = [i for i in range(10000)]
print(lista_c)
print(sys.getsizeof(lista_c))

lista_g = (i for i in range(10000))
print(lista_g)
print(sys.getsizeof(lista_g))

print("===== Fim da ação =====")
time.sleep(3)
os.system("clear")


print("======= Não")
