"""
Faça um programa para calcular números
solicite que o seu usuario digite 4 números
faça a soma do primeiro numero, com o ultimo numero
depois faça a multiplicação, com os números do meio
ao final some o resultado da soma, com o resultado da multiplicação

se o resultado total for > do que 100 mostrar

=========================
O resultado alcançado foi xxx parabéns
=========================

se o resultado total for <= do que 100 mostrar

=========================
O resultado alcançado foi xxx e ficou abaixo da expectativa
=========================
"""
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))
num4 = float(input("Digite um número: "))

soma = num1 + num4
mult = num2 * num3
total = soma + mult

if total >= 100:
  print("===================")
  print(f"O resultado alcançado foi {total} parabéns")
  print("===================")
else:
  print("===================") 
  print(f"O resultado alcançado foi {total} e ficou abaixo da expectativa") 
  print("===================")