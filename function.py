#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

def funcaoSemParametros(): #cria uma função
    print("Uma funcao")
funcaoSemParametros()    

def funcaoComParametros(parametro):#cria a função
    print(parametro + 1)
funcaoComParametros(1)#executa a funcao    

def funcaoComParametrosValorPadrao(parametro = 2): #cria função
    print(parametro +1)
funcaoComParametrosValorPadrao()#executa a funcao

def funcaoComMaisDeUmParametro(numero1, numero2):# cria a função
    print(numero1, numero2, "", 1)
funcaoComMaisDeUmParametro(1,3)#executa a função

def funcaoComRetorno(numero1):#cria funcao
    return numero1 + 1
print(funcaoComRetorno(10))

def funcaoComArrayDeParametros(*args):#cria a funcao
    print(f"Indice 0 - {args[0]}")
    print(args)
funcaoComArrayDeParametros(1,2,3,4,5,6)#executa a funcao    

time.sleep(2)
os.system("clear")

def mostrar(numero):
    return f":: Mostrando uma informação na tela {numero}::"

while True:
    print("+++ Bem Vindo +++")
    print("Digite uma opção:")
    print("1 - Mostrar algo na tela")
    print("2 - Mostrar algo na tela mais 1")
    print("3 - Mostrar algo na tela mais 2")
    print("4 - Mostrar algo na tela mais 3")
    print("5 - Mostrar algo na tela mais 4")
    print("10 - Sair do programa")

    opcao = int(input())
    os.system("clear")

    if opcao == 10:
        break
    elif opcao == 1:
        print(mostrar(""))
    elif opcao == 2:
        print(f"{ mostrar(1) }")
    elif opcao == 3:
        print(f"{ mostrar(2) }")
    elif opcao == 4:
        print(f"{ mostrar(3) }")
    elif opcao == 5:
        print(f"{ mostrar(4) }")
    else:
        print("Opção Inválida")

    time.sleep(2)
    os.system("clear")
    
