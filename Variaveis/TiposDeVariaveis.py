nome = input("Digite o nome de fim funcionario: ")
empresa = input(("Digite o nome da empresa: "))
quantidadeFuncionarios = int(input("Digite a quantidade de funcionarios: "))
mediaMensalidade = float(input("Digite a media da mensalidade: "))

print("*********************************************************")
#o mais faz a concatenação entre string e strings
print(nome + " trabalha na " + empresa)
#a virgula faz a concatenação entre string e numero
print("A empresa possui ", quantidadeFuncionarios)

print("A media da mensalidade é de: " + str(mediaMensalidade))

print("Tipos das variaveis: ")
print("O tipo da variavel [nome] é: ", type(nome))
print("O tipo da variavel [empresa] é: ", type(empresa))
print("O tipo da variavel [quantidadeFuncionarios] é: ", type(quantidadeFuncionarios))
print("O tipo da variavel [mediaMensalidade] é: ", type(mediaMensalidade))
