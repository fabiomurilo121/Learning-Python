v1 = int(input("Valor n1: "))
v2 = int(input("Valor n2: "))
salario = int(input("Informe o salario recebido: "))
porc = int(input("Informe a porcentagem do aumento: "))

s = v1 + v2
m = v1 * v2
d = v1 / v2
di = v1 // v2
e =  v1 ** v2
resu = porc * salario
resu = resu // 100
somaS = resu + salario

print('A soma é {}, A Multiplicação é {}, A divisão é {:.2f},'.format(s,m,d))
print('A divisão por inteiros é {},e a potencia é {}'.format(di,e))
print('O salario ficará {} devido ao aumento de {}'.format(somaS,resu))

