#fluxo: (1- sequencia, 2-seleção, 3-repetição.)
#primeiro linha(horizontal), depois coluna(vertical).
# esquerda dps baixo ajuda no 2048
from random import randint

#criar matriz
def criarMatriz ():
    matriztabuleiro = [0]*9
    for cont in range (9): #vai de 0 até 8
     matriztabuleiro[cont] = [0] * 9
    return (matriztabuleiro)

#mostrar matriz
def mostrarMatriz (matriztabuleiro):
    for linha in range (9):
        for coluna in range (9):
            if (matriztabuleiro[linha][coluna]== -1):
                print("x", end= " | ")
            elif (matriztabuleiro[linha][coluna]== 0):
                print("0", end= " | ")
            elif (matriztabuleiro[linha][coluna]== -2):
                print(" ", end= " | ")
            else:
                print(matriztabuleiro[linha][coluna], end= " | ")
        print() #sem esse print aqui fica tudo baguncado a visibilidade do  usuario

#sortear as bombas aleatoriamente, porém sem repetir
def sortearBomba (matriztabuleiro):
    contadorbomb = 0
    while (contadorbomb<10):
        linha = randint(0, 8) #sortear número de 0 até 8
        coluna = randint(0, 8)
        if (matriztabuleiro[linha][coluna]== 0):
            matriztabuleiro[linha][coluna] = -1 #pra nao cair 2 bombas no mesmo lugar
            contadorbomb += 1 # contadorbomb = contadorbomb + 1

#calcular as dicas
def calcularDicas (matriztabuleiro):
    for linha in range (9):
        for coluna in range (9):
            contadorbomb = 0
            if (matriztabuleiro[linha][coluna] != -1):
                for l in range (linha-1, linha +2, 1): #comeca na linha, varia de -1, até +1, aumentando de 1 em 1
                    for c in range (coluna-1, coluna+2, 1):
                        if (l>=0 and l<=8 and c>= 0 and c<= 8):
                            #print (" Vizinho ",l,",",c)
                            if (matriztabuleiro[l][c] == -1):
                                contadorbomb += 1
                matriztabuleiro[linha][coluna] = contadorbomb

#testar e abrir as casas vazias vizinhas a coordenada
def testarVizinhos (linha, coluna, tab, tela):
    tela[linha][coluna] = -2 #flag para casa visitada - aberta
    for l in range(linha-1, linha+2, 1):
        for c in range (coluna-1, coluna+2, 1):
            if (l>=0 and l<=8 and c>=0 and c<=8):
                if (tab[l][c]==0 and tela[l][c]!=-2):
                    testarVizinhos(l, c, tab, tela)
                elif (tab[l][c]>=1 and tab[l][c]<=8):
                    tela[l][c]= tab[l][c]

# testar o mecanismo pro jogador ganhar ou perder o jogo
def testarVitoria(tab, tela):
    ca = 0
    cc = 0
    for linha in range (9):
        for coluna in range (9):
            if (tab[linha][coluna]==-1 and tela[linha][coluna]==-1):
                ca += 1
            elif (tela[linha][coluna]==-1):
                cc += 1
    if(ca==10 and cc == 0):
        return True
    else:
        return False

#codigo principal
matriztabuleiro = criarMatriz()
tela = criarMatriz()
sortearBomba(matriztabuleiro)
calcularDicas(matriztabuleiro)  #mostrarMatriz(matriztabuleiro)
print("\n")

#atribuicao para perdeu ou ganhou o jogo.
ganhou = False
perdeu = False
while (not ganhou and not perdeu): # PODE SER TB --> while (ganhou == False and perdeu == False):
    #mostrarMatriz(matriztabuleiro) # pode tirar se quiser, isso e so pra testar se ta funcionando
    print("Tela, matriz do jogador: ")
    mostrarMatriz(tela)
    print()
    linha = int(input("Linha : "))
    coluna = int(input("Coluna : "))
    opcao = input("<A> para Abrir casa ou <B> para marcar Bomba : ")
    print (opcao)
    if (opcao == "B" or opcao == "b"):
        tela[linha][coluna] = -1
        ganhou = testarVitoria(matriztabuleiro, tela)
    elif (opcao == "A" or opcao == "a"):
        if(matriztabuleiro[linha][coluna == -1]):
            print ("Explodiu :( ")
            perdeu = True
        elif(matriztabuleiro[linha][coluna] >= 1 and matriztabuleiro[linha][coluna] <= 8):
            tela[linha][coluna] = matriztabuleiro[linha][coluna]
        else:
            testarVizinhos (linha, coluna, matriztabuleiro, tela)
        ganhou = testarVitoria(matriztabuleiro, tela)

if (ganhou):
    print("Parabens !!")