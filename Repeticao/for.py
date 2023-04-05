tabuada = int(input("Digite um numero para saber a taboada dele: "))
print("Taboada do numero: ", tabuada)
            # inicio, fim, incremento
for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada * valor)))
