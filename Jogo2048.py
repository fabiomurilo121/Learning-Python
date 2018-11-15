#introdução ao jogo e tuturial
from random import randint, sample

print("=-"*30)
print("         >>>>>>>>>> Bem vindo ao 2048 !!!! <<<<<<<<<<")
print("-="*30)
def criarMatriz():
    matrizTab = [0]*4           #ou matrizTab = [[0,0,0,0],
    for cont in range(4):       #                [0,0,0,0],
        matrizTab[cont] = [0]*4 #                [0,0,0,0],
    return matrizTab            #                [0,0,0,0]]
def sortearCasaInicio (matrizTab):
    num = 0
    while (num<2):
        l = randint(0,3)
        c = randint(0,3)
        if (matrizTab[l][c] == 0):
            sorteioNum = sample([2, 4], 1)
            matrizTab[l][c] = sorteioNum
            num += 1
def aposMover (matrizTab):
    while True:
        l = randint(0, 3)
        c = randint(0, 3)
        if (matrizTab[l][c] == 0):
            sorteioNum = sample([2, 4], 1)
            matrizTab[l][c] = sorteioNum
            break


def mostrarMatriz(matrizTab):
    for l in range (0,4): #linha
        for c in range(0,4): #coluna
            if matrizTab[l][c]==(0 or 1 or 3):
                print("[0]", end = "    ")
            elif matrizTab[l][c]!= (0 or 1 or 3):
                num = matrizTab[l][c]
                if type(num) == list:
                    print(num, end = "    ")
                else:
                    print(f"[{num}]", end = "    ")
        print()
def moverCima(matrizTab):
    a = 0
    for l in range(4):
        for c in range(4):
            if l >= 1:
                while True:
                    if matrizTab[l][c] == 0:
                        break
                    elif matrizTab[l][c] == 1 and l ==1:
                        matrizTab[l][c] = 0
                    elif matrizTab[l][c] == 3 and l ==2:
                        matrizTab[l][c] = 0

                    elif matrizTab[l][c] != (0 or 1 or 3):
                        if matrizTab[l-1][c] == 0:
                            matrizTab[l-1][c] = matrizTab[l][c]
                            matrizTab[l][c] = 1
                            a = 1
                            if l == 1:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l-1][c] == matrizTab[l][c]:
                            soma = matrizTab[l-1][c]
                            soma2 = matrizTab[l][c]
                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l-1][c] = somaT
                            matrizTab[l][c] = 1
                            a = 1
                            if l ==1:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l-1][c] != 0:
                            break
                        else:
                            continue
                    elif l >= 2 and matrizTab[l][c] == 1:
                        if matrizTab[l - 2][c] == 0:
                            matrizTab[l - 2][c] = matrizTab[l - 1][c]
                            matrizTab[l - 1][c] = 0
                            matrizTab[l][c] = 3
                            a = 1
                            if l == 2:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l - 2][c] == matrizTab[l - 1][c]:
                            soma = matrizTab[l - 1][c]
                            soma2 = matrizTab[l - 2][c]

                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l-2][c] = somaT
                            matrizTab[l-1][c] = 0
                            matrizTab[l][c] = 3
                            a = 1
                            if l == 2:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l-2][c] != 0:
                            break

                        if l == 2:
                            break
                        else:
                            continue
                    elif  l== 3 and matrizTab[l][c] == 3:
                        if matrizTab[l-3][c] == 0:
                            matrizTab[l-3][c] = matrizTab[l-2][c]
                            matrizTab[l-2][c] = 0
                            matrizTab[l][c] = 0
                            a = 1
                            continue
                        elif matrizTab[l-3][c] == matrizTab[l-2][c]:
                            soma = matrizTab[l-2][c]
                            soma2 = matrizTab[l-3][c]

                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l-3][c] = somaT
                            matrizTab[l-2][c] = 0
                            matrizTab[l][c] = 0
                            a = 1
                            continue
                        if l == 3:
                            break
                    if matrizTab[l][c] == (1 or 3):
                        matrizTab[l][c] = 0
                        continue
                    else:
                        break
                if matrizTab[l][c] == (1 or 3):
                    matrizTab[l][c] = 0
            if matrizTab[l][c] == (1 or 3):
                matrizTab[l][c] = 0
    return a

def moverBaixo(matrizTab):
    a = 0
    for l in range(4):
        for c in range(4):
            if l < 3:
                while True:
                    if matrizTab[l][c] == 0:
                        break
                    elif matrizTab[l][c] == 1 and l ==2:
                        matrizTab[l][c] = 0
                    elif matrizTab[l][c] == 3 and l ==1:
                        matrizTab[l][c] = 0

                    elif matrizTab[l][c] != (0 or 1 or 3):
                        if matrizTab[l+1][c] == 0:
                            matrizTab[l+1][c] = matrizTab[l][c]
                            matrizTab[l][c] = 1
                            a = 1
                            if l == 2:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l+1][c] == matrizTab[l][c]:
                            soma = matrizTab[l+1][c]
                            soma2 = matrizTab[l][c]
                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l+1][c] = somaT
                            matrizTab[l][c] = 1
                            a = 1
                            if l ==2:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l+1][c] != 0:
                            break
                        else:
                            continue
                    elif l < 2 and matrizTab[l][c] == 1:
                        if matrizTab[l + 2][c] == 0:
                            matrizTab[l + 2][c] = matrizTab[l + 1][c]
                            matrizTab[l + 1][c] = 0
                            matrizTab[l][c] = 3
                            a = 1
                            if l == 1:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l + 2][c] == matrizTab[l + 1][c]:
                            soma = matrizTab[l + 1][c]
                            soma2 = matrizTab[l + 2][c]

                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l+2][c] = somaT
                            matrizTab[l+1][c] = 0
                            matrizTab[l][c] = 3
                            a = 1
                            if l == 1:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l+2][c] != 0:
                            break

                        if l == 1:
                            break
                        else:
                            continue
                    elif  l== 0 and matrizTab[l][c] == 3:
                        if matrizTab[l+3][c] == 0:
                            matrizTab[l+3][c] = matrizTab[l+2][c]
                            matrizTab[l+2][c] = 0
                            matrizTab[l][c] = 0
                            a = 1
                            continue
                        elif matrizTab[l+3][c] == matrizTab[l+2][c]:
                            soma = matrizTab[l+2][c]
                            soma2 = matrizTab[l+3][c]

                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l+3][c] = somaT
                            matrizTab[l+2][c] = 0
                            matrizTab[l][c] = 0
                            a = 1
                            continue
                        if l == 0:
                            break
                    if matrizTab[l][c] == (1 or 3):
                        matrizTab[l][c] = 0
                        continue
                    else:
                        break
                if matrizTab[l][c] == (1 or 3):
                    matrizTab[l][c] = 0
            if matrizTab[l][c] == (1 or 3):
                matrizTab[l][c] = 0
    return a

def moverDireita(matrizTab):
    a = 0
    for l in range(4):
        for c in range(4):
            if c < 3:
                while True:
                    if matrizTab[l][c] == 0:
                        break
                    elif matrizTab[l][c] == 1 and c ==2:
                        matrizTab[l][c] = 0
                    elif matrizTab[l][c] == 3 and c ==1:
                        matrizTab[l][c] = 0

                    elif matrizTab[l][c] != (0 or 1 or 3):
                        if matrizTab[l][c+1] == 0:
                            matrizTab[l][c+1] = matrizTab[l][c]
                            matrizTab[l][c] = 1
                            a = 1
                            if c == 2:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l][c+1] == matrizTab[l][c]:
                            soma = matrizTab[l][c+1]
                            soma2 = matrizTab[l][c]
                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l][c+1] = somaT
                            matrizTab[l][c] = 1
                            a = 1
                            if c ==2:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l][c+1] != 0:
                            break
                        else:
                            continue
                    elif c < 2 and matrizTab[l][c] == 1:
                        if matrizTab[l][c+2] == 0:
                            matrizTab[l][c+2] = matrizTab[l][c+1]
                            matrizTab[l][c+1] = 0
                            matrizTab[l][c] = 3
                            a = 1
                            if c == 1:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l][c+2] == matrizTab[l][c+1]:
                            soma = matrizTab[l][c+1]
                            soma2 = matrizTab[l][c+2]

                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l][c+2] = somaT
                            matrizTab[l][c+1] = 0
                            matrizTab[l][c] = 3
                            a = 1
                            if c == 1:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l][c+2] != 0:
                            break

                        if c == 1:
                            break
                        else:
                            continue
                    elif  c== 0 and matrizTab[l][c] == 3:
                        if matrizTab[l][c+3] == 0:
                            matrizTab[l][c+3] = matrizTab[l][c+2]
                            matrizTab[l][c+2] = 0
                            matrizTab[l][c] = 0
                            a = 1
                            continue
                        elif matrizTab[l][c+3] == matrizTab[l][c+2]:
                            soma = matrizTab[l][c+2]
                            soma2 = matrizTab[l][c+3]

                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l][c+3] = somaT
                            matrizTab[l][c+2] = 0
                            matrizTab[l][c] = 0
                            a = 1
                            continue
                        if c == 0:
                            break
                    if matrizTab[l][c] == (1 or 3):
                        matrizTab[l][c] = 0
                        continue
                    else:
                        break
                if matrizTab[l][c] == (1 or 3):
                    matrizTab[l][c] = 0
            if matrizTab[l][c] == (1 or 3):
                matrizTab[l][c] = 0
    return a

def moverEsquerda(matrizTab):
    a = 0
    for l in range(4):
        for c in range(4):
            if c >= 1:
                while True:
                    if matrizTab[l][c] == 0:
                        break
                    elif matrizTab[l][c] == 1 and c ==1:
                        matrizTab[l][c] = 0
                    elif matrizTab[l][c] == 3 and c ==2:
                        matrizTab[l][c] = 0

                    elif matrizTab[l][c] != (0 or 1 or 3):
                        if matrizTab[l][c-1] == 0:
                            matrizTab[l][c-1] = matrizTab[l][c]
                            matrizTab[l][c] = 1
                            a = 1
                            if c == 1:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l][c-1] == matrizTab[l][c]:
                            soma = matrizTab[l][c-1]
                            soma2 = matrizTab[l][c]
                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l][c-1] = somaT
                            matrizTab[l][c] = 1
                            a = 1
                            if c ==1:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l][c-1] != 0:
                            break
                        else:
                            continue
                    elif c >= 2 and matrizTab[l][c] == 1:
                        if matrizTab[l][c-2] == 0:
                            matrizTab[l][c-2] = matrizTab[l][c-1]
                            matrizTab[l][c-1] = 0
                            matrizTab[l][c] = 3
                            a = 1
                            if c == 2:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l][c-2] == matrizTab[l][c-1]:
                            soma = matrizTab[l][c-1]
                            soma2 = matrizTab[l][c-2]

                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l][c-2] = somaT
                            matrizTab[l][c-1] = 0
                            matrizTab[l][c] = 3
                            a = 1
                            if c == 2:
                                matrizTab[l][c] = 0
                            continue
                        elif matrizTab[l][c-2] != 0:
                            break

                        if c == 2:
                            break
                        else:
                            continue
                    elif  c== 3 and matrizTab[l][c] == 3:
                        if matrizTab[l][c-3] == 0:
                            matrizTab[l][c-3] = matrizTab[l][c-2]
                            matrizTab[l][c-2] = 0
                            matrizTab[l][c] = 0
                            a = 1
                            continue
                        elif matrizTab[l][c-3] == matrizTab[l][c-2]:
                            soma = matrizTab[l][c-2]
                            soma2 = matrizTab[l][c-3]

                            if type (soma) != list:
                                inteiro = soma
                                somaT = inteiro
                            elif type (soma) == list:
                                lista = soma[0]
                                somaT = lista
                            if type (soma2) != list:
                                inteiro2 = soma2
                                somaT = inteiro2 + somaT
                            elif type (soma2) == list:
                                lista2 = soma[0]
                                somaT = lista2 + somaT

                            matrizTab[l][c-3] = somaT
                            matrizTab[l][c-2] = 0
                            matrizTab[l][c] = 0
                            a = 1
                            continue
                        if c == 3:
                            break
                    if matrizTab[l][c] == (1 or 3):
                        matrizTab[l][c] = 0
                        continue
                    else:
                        break
                if matrizTab[l][c] == (1 or 3):
                    matrizTab[l][c] = 0
            if matrizTab[l][c] == (1 or 3):
                matrizTab[l][c] = 0
    return a

#comeco = int(input("Pressione (1) para ler o tuturial ou (2) para iniciar direto: "))
comeco = 2
if comeco == 1:
    print("\n")
    print("2048 é um jogo de raciocínio imperdível por sua mistura de movimentos simples com a necessidade de boa estratégia e inteligência. Mova os quadrados para os lados e some potências de 2 até atingir")
    print("2048 pontos em uma única casa, somente serão somados casas com valores iguais, ex: (2 com 2), (8 com 8), cuidado para não preencher todas as casas ou sera GAME OVER !!.")
    print("\n")
    while comeco != 2:
        pronto = input("Está pronto para começar a jogar? <S> ou <N>: ")
        if pronto == ("s"or"S"):
            comeco = 2

#começo real do jogo
if comeco == 2:
    matrizTab = criarMatriz()
    sortearCasaInicio(matrizTab)
    mostrarMatriz(matrizTab)
    a = 3
    b = 3
    c = 3
    d = 3
    z = 0
    while (z == 0):
        escolha = input("Digite para qual direção deseja mover as casas (<W> = CIMA), (<S> = BAIXO), (<D> = DIREITA), (<A> = ESQUERDA): ")

        if escolha == ("w" or "W"):
            a = moverCima(matrizTab)
            if a != 0:
                aposMover(matrizTab)
                print()
                mostrarMatriz(matrizTab)
            else:
                print()
                mostrarMatriz(matrizTab)
        if escolha == ("s" or "S"):
            b = moverBaixo(matrizTab)
            if b != 0:
                aposMover(matrizTab)
                print()
                mostrarMatriz(matrizTab)
            else:
                print()
                mostrarMatriz(matrizTab)
        if escolha == ("d" or "D"):
            c = moverDireita(matrizTab)
            if c != 0:
                aposMover(matrizTab)
                print()
                mostrarMatriz(matrizTab)
            else:
                print()
                mostrarMatriz(matrizTab)
        if escolha == ("a" or "A"):
            d = moverEsquerda(matrizTab)
            if d != 0:
                aposMover(matrizTab)
                print()
                mostrarMatriz(matrizTab)
            else:
                print()
                mostrarMatriz(matrizTab)
        # derrota
        if a == 0:
            if b == 0:
                if c == 0:
                    if d == 0:
                        print("Game Over")
                        z = 1


        #vitória
        for l in range(4):
            for c in range(4):
                if matrizTab[l][c] == 2048:
                    print("Você GANHOU !!!!")
                    z = 1