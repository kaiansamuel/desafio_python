import os
while True:
  numero = int(input("Digite 0 para sair:\n"))
  print(f"Você digitou o {numero} número")
  if numero == 0:
    break
  
print("Exemplo for")
inicial = int(input("Digite o número inicial:\n"))
final = int(input("Digite o numero final:\n"))
os.system('clear')
for x in range(inicial, final):
  print(f'Numero {x}')