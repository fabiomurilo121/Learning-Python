print('-'*40)
n = int(input("Entre com a quantidade de termos que quer mostrar: "))
print('-'*40)

t1 = 0
t2 = 1

print("{} -> {}".format(t1,t2),end='')

count = 3

while count <=n:
    t3 = t1 +t2
    print(' -> {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    count += 1
print('-> FIM')