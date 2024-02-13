print("Digite um nome: ")
nome = input().lower().strip()

if nome == "Leandro":
  print("Nome encontrado")
elif nome.find("danilo") != -1 or nome =="kaian":
  print("Encontrei o nome procurado!")  
else:
  print("Nome não encontrado")  