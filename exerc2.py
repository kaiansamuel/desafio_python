print("==== Sistema de combustível =====")
padrao = float(input('Digite a quantidade de litros padrão: '))
total = float(input("Digite a quantidade de litros para preencher a quantidade total: "))
print(f"A quantidade de litros que ficou no posto foi: {total}" )
total_porcentagem = total  / padrao * 100
print("Estamos com a capacidade de {:0.2f}% em nossos tanques".format(total_porcentagem))

print("==== Chegou um cliente, bora vender? ====")
nomeCliente = input("Digite o nome do cliente: ")
valorCliente = int(input("Digite quantos litros o sr deseja colocar: "))
print(f"::::: Ficou com {total - valorCliente}  litros no posto!::::::")