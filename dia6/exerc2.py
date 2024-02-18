"""
Claudio é um matemático que precisa de um programa para facilitar
o calulo de uma tabuada, faça um programa que solicite 1 número multiplicador
e 1 número do iterador. Crie a tabuada do mesmo, exemplo:

Digite um numero para calcular a tabuada?
5
Digite um numero para o iterador da tabuada
3

1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
"""

print("======== Programa de calculo da tabuada =======")
numero = int(input("Digite um numero\n"))
iterador = int(input("Digite o numero a ser multiplicado\n"))

# utilizando o while

print("========== while ==========")
i = 1
while i <= iterador:
  print(f"{i} x {numero} = {numero * i}")
  i+= 1

# utilizando o for

print("=========== for ===========")
for i in range(1, iterador + 1):
  print(f"{i} x {numero} = {numero * i}")
    