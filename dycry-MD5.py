import random
import hashlib
import time

hash = input("entre com seu Hash: ")
rand = input("entre com os caracteres da chave")

inicio = time.time()
v = True
while v == True:
    types = "md5"
    for i in range(1,10**len(rand)):
        r = ''.join(random.choice(rand)for i in range(len(rand)))
        try:
            d = hashlib.new(types)
            v = False
        except:
            continue
        d.update(r.encode())
        f = d.hexdigest()

        print('[-'+ r + '/t'+f)
        if f == hash:
            print("\n[*]"+ r + "/t"+f)
            break
if f != hash:
    print("Tente outra palavra!")

fim = time.time()
diferenca = fim - inicio
print(diferenca)