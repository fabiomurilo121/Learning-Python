x = int(input("Informe o numero da tabuada: "))


for i in range(0,11,1):
    resu = i * x
    print('{} x {} = {}'.format(x,i,resu))