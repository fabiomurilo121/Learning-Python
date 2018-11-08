import hashlib
import os
import random
import time

login1 = input("login: ")
senha1 = input("senha: ")

login2 = input("login: ")
senha2 = input("senha: ")

login3 = input("login: ")
senha3 = input("senha: ")

login4 = input("login: ")
senha4 = input("senha: ")

'''def diminuir(str):
    max = 4 # Numero Maximo de caracteres Permitidos.
    if len(str) > max:
        return str[:max]
    else:
        return str

var = diminuir(login1)
print(var)'''

def ds(text):
    textUtf8 = text.encode("utf-8")
    hash = hashlib.md5( textUtf8 )
    hexa = hash.hexdigest()
    print("senha em MD5 fica: " + hexa)
    return hexa

recebe1 = ds(senha1)
recebe2 = ds(senha2)
recebe3 = ds(senha3)
recebe4 = ds(senha4)

'''def cifraCesar(entrada): Para modificar o tipo do Hash
    aq = []
    chave = 3
    for cont in range(len(entrada)):
        if entrada[cont] == " ":
            aq.append(" ")
        else:
            crip = ord(entrada[cont])
            crip = chr(crip + chave)
            aq.append(crip)
            stringA = "".join(aq)
    return stringA

cifra1 = cifraCesar(recebe1)
cifra2 = cifraCesar(recebe2)
cifra3 = cifraCesar(recebe3)
cifra4 = cifraCesar(recebe4)'''


def senha():
    stringSalva =  recebe1 +"\n"+ recebe2 +"\n"+ recebe3 +"\n"+ recebe4
    nomeArquivo = "senha" + ".txt"
    myFile = open(nomeArquivo,'w')
    myFile.write(stringSalva)
    myFile.close()
senha()

def login():
    stringSalva =  login1 +"\n"+ login2 +"\n"+ login3 +"\n"+ login4
    nomeArquivo = "login" + ".txt"
    myFile = open(nomeArquivo,'w')
    myFile.write(stringSalva)
    myFile.close()
login()

def descifra():

    hash = input("entre com seu Hash: ")
    rand = input("entre com os caracteres da chave")

    inicio = time.time()
    v = True
    while v == True:
        types = input("Tipo de codificação")
        for i in range(1, 10 ** len(rand)):
            r = ''.join(random.choice(rand) for i in range(len(rand)))
            try:
                d = hashlib.new(types)
                v = False
            except:
                continue
            d.update(r.encode())
            f = d.hexdigest()

            print('[-' + r + '/t' + f)
            if f == hash:
                print("\n[*]" + r + "/t" + f)
                break
    if f != hash:
        print("Tente outra palavra!")

    fim = time.time()
    diferenca = fim - inicio
    print(diferenca)
