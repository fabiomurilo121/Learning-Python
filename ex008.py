dias = int(input("Quantos dias ficou com o carro ? "))
km = float(input("Quantos KM voce rodou ? "))

calculaDias = dias * 60
calculaKM = km * 0.15

resultado = calculaDias + calculaKM

print("O Valor fica R${} ".format(resultado))