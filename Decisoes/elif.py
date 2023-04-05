nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 21:
    print(nome + ", voce é adulto")
elif idade >= 16:
    print(nome + ", voce é adolecente")
else:
    print(nome + ", voce é crianca")
