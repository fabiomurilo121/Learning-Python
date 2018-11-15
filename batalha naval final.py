jogarnovamente = 1
from time import sleep
while jogarnovamente == 1:
    def imprimirCampoTeste(campo):
        print(
            '\t' * 2 + '1' + '\t' + '2' + '\t' + '3' + '\t' + '4' + '\t' + '5' + '\t' + '6' + '\t' + '7' + '\t' + '8' + '\t' + '9' + '\t' + '10' + '\t' + '11' + '\t' + '12' + '\t' + '13' + '\t' + '14' + '\t' + '15' + '\t' + '16' + '\t' + '17' + '\t' + '18' + '\t' + '19' + '\t' + '20')
        for i in range(20):
            print('\t' + chr(65 + i) + '\t' + campo[i][1] + '\t' + campo[i][2] + '\t' + campo[i][3] + '\t' + campo[i][
                4] + '\t' + campo[i][5] + '\t' + campo[i][6] + '\t' + campo[i][7] + '\t' + campo[i][8] + '\t' +
                  campo[i][
                      9] + '\t' + campo[i][10] + '\t' + campo[i][11] + '\t' + campo[i][12] + '\t' + campo[i][
                      13] + '\t' +
                  campo[i][14] + '\t' + campo[i][15] + '\t' + campo[i][16] + '\t' + campo[i][17] + '\t' + campo[i][
                      18] + '\t' + campo[i][19] + '\t' + campo[i][20])


    def imprimirCampo(campo):
        for linha in range(0, 20, 1):
            for i in range(1, 21, 1):
                if campo[linha][i] == 'n' or campo[linha][i] == 'p' or campo[linha][i] == 'q':
                    campo[linha][i] = '~'

        print(
            '\t' * 2 + '1' + '\t' + '2' + '\t' + '3' + '\t' + '4' + '\t' + '5' + '\t' + '6' + '\t' + '7' + '\t' + '8' + '\t' + '9' + '\t' + '10' + '\t' + '11' + '\t' + '12' + '\t' + '13' + '\t' + '14' + '\t' + '15' + '\t' + '16' + '\t' + '17' + '\t' + '18' + '\t' + '19' + '\t' + '20')
        for i in range(20):
            print('\t' + chr(65 + i) + '\t' + campo[i][1] + '\t' + campo[i][2] + '\t' + campo[i][3] + '\t' + campo[i][
                4] + '\t' + campo[i][5] + '\t' + campo[i][6] + '\t' + campo[i][7] + '\t' + campo[i][8] + '\t' +
                  campo[i][9] + '\t' + campo[i][10] + '\t' + campo[i][11] + '\t' + campo[i][12] + '\t' + campo[i][
                      13] + '\t' + campo[i][14] + '\t' + campo[i][15] + '\t' + campo[i][16] + '\t' + campo[i][
                      17] + '\t' + campo[i][18] + '\t' + campo[i][19] + '\t' + campo[i][20])


    def corrigirCoordenadaTiro(coordenadas):
        linhasPossiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't']
        colunasPossiveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(coordenadas) == 2 or len(coordenadas) == 3:
            if coordenadas[0] in linhasPossiveis:
                if len(coordenadas) == 3:
                    if coordenadas[1] == '1' or coordenadas[1] == '2':
                        if coordenadas[1] == 2:
                            if coordenadas[2] == '0':
                                return True
                            else:
                                return False
                        elif coordenadas[1] == 1:
                            if coordenadas[2] in colunasPossiveis:
                                return True
                            else:
                                return False
                    else:
                        return False
                elif len(coordenadas) == 2:
                    if coordenadas[1] != '0':
                        if coordenadas[1] in colunasPossiveis:
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False


    def corrigirPosicaoTiro(campo, coordenadaLinha, coordenadaColuna):
        for i in range(20):
            if campo[i][0] == coordenadaLinha:
                if campo[i][int(coordenadaColuna)] == '~' or campo[i][int(coordenadaColuna)] == 'n' or campo[i][
                    int(coordenadaColuna)] == 'q' or campo[i][int(coordenadaColuna)] == 'p':
                    return True
                else:
                    return False


    def traduzirCoordenadasLinha(coordenadas):
        letra = coordenadas[0]
        return letra.upper()


    def traduzirCoordenadasColuna(coordenadas):
        coluna = coordenadas.replace(coordenadas[0], "")
        return coluna


    def atirar(campo, coordenadaLinha, coordenadaColuna):
        for i in range(20):
            if campo[i][0] == coordenadaLinha:
                break
        if campo[i][int(coordenadaColuna)] == '~':
            campo[i][int(coordenadaColuna)] = 'O'
            print('Errou !! só tinha Água ')
        elif campo[i][int(coordenadaColuna)] == 'n' or campo[i][int(coordenadaColuna)] == 'q' or campo[i][
            int(coordenadaColuna)] == 'p':
            campo[i][int(coordenadaColuna)] = 'X'
            print('FOGO !! Acertou em cheio ')
        return campo


    # def calcularPontuacao

    def corrigirCoordenadaFragata(coordenadas):
        linhasPossiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't']
        colunasPossiveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(coordenadas) == 2 or len(coordenadas) == 3:
            if coordenadas[0] in linhasPossiveis:
                if len(coordenadas) == 3:
                    if coordenadas[1] == '1':
                        if coordenadas[2] in colunasPossiveis:
                            return True
                        else:
                            return False
                    else:
                        return False
                elif len(coordenadas) == 2:
                    if coordenadas[1] != '0':
                        if coordenadas[1] in colunasPossiveis:
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False


    def corrigirPosicaoFragata(campo, coordenadaLinha, coordenadaColuna):
        for i in range(20):
            if campo[i][0] == coordenadaLinha:
                break
        if campo[i][int(coordenadaColuna)] == '~' and campo[i][int(coordenadaColuna) + 1] == '~':
            return True
        else:
            return False


    def posicionarFragata(campo, coordenadaLinha, coordenadaColuna):
        for i in range(20):
            linha = i
            if campo[i][0] == coordenadaLinha:
                break
        campo[linha][int(coordenadaColuna)] = 'n'
        campo[linha][int(coordenadaColuna) + 1] = 'n'
        return campo


    def corrigirCoordenadasCruzador(coordenadas):
        linhasPossiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't']
        colunasPossiveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(coordenadas) == 2 or len(coordenadas) == 3:
            if coordenadas[0] in linhasPossiveis:
                if len(coordenadas) == 3:
                    if coordenadas[1] == '1':
                        if coordenadas[2] in colunasPossiveis and coordenadas[2] != '9':
                            return True
                        else:
                            return False
                    else:
                        return False
                elif len(coordenadas) == 2:
                    if coordenadas[1] != '0':
                        if coordenadas[1] in colunasPossiveis:
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False


    def corrigirPosicaoCruzador(campo, coordenadaLinha, coordenadaColuna):
        for i in range(20):
            if campo[i][0] == coordenadaLinha:
                break
        if campo[i][int(coordenadaColuna)] == '~' and campo[i][int(coordenadaColuna) + 1] == '~' and campo[i][
            int(coordenadaColuna) + 2] == '~':
            return True
        else:
            return False


    def posicionarCruzador(campo, coordenadaLinha, coordenadaColuna):
        for i in range(20):
            linha = i
            if campo[i][0] == coordenadaLinha:
                break
        campo[linha][int(coordenadaColuna)] = 'q'
        campo[linha][int(coordenadaColuna) + 1] = 'q'
        campo[linha][int(coordenadaColuna) + 2] = 'q'
        return campo


    def corrigirCoordenadasPorta(coordenadas):
        linhasPossiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't']
        colunasPossiveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(coordenadas) == 2 or len(coordenadas) == 3:
            if coordenadas[0] in linhasPossiveis:
                if len(coordenadas) == 3:
                    if coordenadas[1] == '1':
                        if coordenadas[2] in colunasPossiveis and coordenadas[2] != '9' and coordenadas[2] != '8':
                            return True
                        else:
                            return False
                    else:
                        return False
                elif len(coordenadas) == 2:
                    if coordenadas[1] != '0':
                        if coordenadas[1] in colunasPossiveis:
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False


    def corrigirPosicaoPorta(campo, coordenadaLinha, coordenadaColuna):
        for i in range(20):
            if campo[i][0] == coordenadaLinha:
                break
        if campo[i][int(coordenadaColuna)] == '~' and campo[i][int(coordenadaColuna) + 1] == '~' and campo[i][
            int(coordenadaColuna) + 2] == '~' and campo[i][int(coordenadaColuna) + 3] == '~':
            return True
        else:
            return False


    def posicionarPorta(campo, coordenadaLinha, coordenadaColuna):
        for i in range(20):
            linha = i
            if campo[i][0] == coordenadaLinha:
                break
        campo[linha][int(coordenadaColuna)] = 'p'
        campo[linha][int(coordenadaColuna) + 1] = 'p'
        campo[linha][int(coordenadaColuna) + 2] = 'p'
        campo[linha][int(coordenadaColuna) + 3] = 'p'
        return campo


    def pontuacaoFragata(campo, linhaFrUm, colunaFrUm, linhaFrDois, colunaFrDois, linhaFrTres, colunaFrTres,
                         linhaFrQuatro, colunaFrQuatro, linhaFrCinco, colunaFrCinco):
        afundados = 0
        for a in range(20):  # fragata 1
            if campo[a][0] == linhaFrUm:
                break
        if campo[a][int(colunaFrUm)] == 'X' and campo[a][int(colunaFrUm) + 1] == 'X':
            afundados += 1
        for b in range(20):  # fragata 2
            if campo[b][0] == linhaFrDois:
                break
        if campo[b][int(colunaFrDois)] == 'X' and campo[b][int(colunaFrDois) + 1] == 'X':
            afundados += 1
        for c in range(20):  # fragata 3
            if campo[c][0] == linhaFrTres:
                break
        if campo[c][int(colunaFrTres)] == 'X' and campo[c][int(colunaFrDois) + 1] == 'X':
            afundados += 1
        for d in range(20):  # fragata 4
            if campo[d][0] == linhaFrQuatro:
                break
        if campo[d][int(colunaFrQuatro)] == 'X' and campo[d][int(colunaFrQuatro) + 1] == 'X':
            afundados += 1
        for e in range(20):  # fragata 5
            if campo[e][0] == linhaFrCinco:
                break
        if campo[e][int(colunaFrCinco)] == 'X' and campo[e][int(colunaFrCinco) + 1] == 'X':
            afundados += 1

        print(afundados, 'Fragatas afundada(s)')
        pontuacao = afundados * 10
        return pontuacao


    def pontuacaoCruzador(campo, linhaCrUm, colunaCrUm, linhaCrDois, colunaCrDois, linhaCrTres, colunaCrTres,
                          linhaCrQuatro, colunaCrQuatro):
        afundados = 0
        for a in range(20):  # cruzador 1
            if campo[a][0] == linhaCrUm:
                break
        if campo[a][int(colunaCrUm)] == 'X' and campo[a][int(colunaCrUm) + 1] == 'X' and campo[a][
            int(colunaCrUm) + 2] == 'X':
            afundados += 1
        for b in range(20):  # cruzador 2
            if campo[b][0] == linhaCrDois:
                break
        if campo[b][int(colunaCrDois)] == 'X' and campo[b][int(colunaCrDois) + 1] == 'X' and campo[b][
            int(colunaCrDois) + 2] == 'X':
            afundados += 1
        for c in range(20):  # cruzador 3
            if campo[c][0] == linhaCrTres:
                break
        if campo[c][int(colunaCrTres)] == 'X' and campo[c][int(colunaCrDois) + 1] == 'X' and campo[c][
            int(colunaCrDois) + 2] == 'X':
            afundados += 1
        for d in range(20):  # cruzador 4
            if campo[d][0] == linhaCrQuatro:
                break
        if campo[d][int(colunaCrQuatro)] == 'X' and campo[d][int(colunaCrQuatro) + 1] == 'X' and campo[d][
            int(colunaCrQuatro) + 2] == 'X':
            afundados += 1

        print(afundados, 'Cruzadores afundado(s)')
        pontuacao = afundados * 20
        return pontuacao


    def pontuacaoPorta(campo, linhaPoUm, colunaPoUm, linhaPoDois, colunaPoDois, linhaPoTres, colunaPoTres):
        afundados = 0
        for a in range(20):  # porta 1
            if campo[a][0] == linhaPoUm:
                break
        if campo[a][int(colunaPoUm)] == 'X' and campo[a][int(colunaPoUm) + 1] == 'X' and campo[a][
            int(colunaPoUm) + 2] == 'X' and campo[a][int(colunaPoUm) + 3] == 'X':
            afundados += 1
        for b in range(20):  # porta 2
            if campo[b][0] == linhaPoDois:
                break
        if campo[b][int(colunaPoDois)] == 'X' and campo[b][int(colunaPoDois) + 1] == 'X' and campo[b][
            int(colunaPoDois) + 2] == 'X' and campo[b][int(colunaPoDois) + 3] == 'X':
            afundados += 1
        for c in range(20):  # porta 3
            if campo[c][0] == linhaPoTres:
                break
        if campo[c][int(colunaPoTres)] == 'X' and campo[c][int(colunaPoTres) + 1] == 'X' and campo[c][
            int(colunaPoTres) + 2] == 'X' and campo[c][int(colunaPoTres) + 3] == 'X':
            afundados += 1

        print(afundados, 'Porta aviões afundado(s)')
        pontuacao = afundados * 30
        return pontuacao


    def calcularPontuacao(pontuacaoFragata, pontuacaoCruzador, pontuacaoPorta):
        pontuacaoTotal = pontuacaoFragata + pontuacaoCruzador + pontuacaoPorta
        print(' Pontos [', pontuacaoTotal, ']')
        return pontuacaoTotal


    campo = [['A', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['B', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['C', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['D', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['E', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['F', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['G', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['H', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['I', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['J', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['K', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['L', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['M', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['N', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['O', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['P', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['Q', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['R', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['S', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
             ['T', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

    # posicionar as fragatas
    print("=-" * 13)
    print("Bem Vindo à Batalha Naval")
    print("-=" * 13)
    tuturial = str(input("Deseja ver o Tuturial? digite Y (MAIÚSCULO) para sim ou N (MAIÚSCULO) para não :"))
    while tuturial != "Y" and tuturial != "N":
        tuturial = str(input("Deseja ver o Tuturial? digite Y(MAIÚSCULO) para sim ou N(MAIÚSCULO) para não :"))
        if tuturial == "Y" and tuturial == "N":
            continue

    if tuturial == "Y":
        sleep(1)
        print("Objetivo do jogo:-Um jogador disporá o tabuleiro e o segundo tentará acertar")
        sleep(1)
        print(
            "Regras do jogo : -Um jogador dispõe seus navios (sempre na horizontal) e outro tenta acertá-los informando o código de uma célula. Sempre começando por uma letra minúscula seguida de um número.                       Exemplo: a8")
        sleep(1)
        print(
            "                -Os navios disponíveis são: 3 Porta aviões, que ocupam 4 casas cada um, e valem 30 pontos por cada abate.")
        sleep(1)
        print(
            "                                            4 Cruzadores, que ocupam 3 casas cada um, e valem 20 pontos por cada abate.")
        sleep(1)
        print(
            "                                            5 Fragatas, que ocupam 2 casas cada um, e valem 10 pontos por cada abate.")
        sleep(1)
        print(
            "                -A matriz do sistema contem 20 linhas e 20 colunas, sendo as linhas entre [a] e [t] e as colunas entre [1] a [20]")
        sleep(1)
        print(
            "                -Toda localização dos barcos digitado pelo jogador um, será completada pela direita, exemplo, se o jogar colocar uma Fragata na posição a1, a outra parte irá automáticamente para a2,                 assim sendo, não será possível jogar aos extremos do canto direito do mapa.")
        sleep(1)
        print(
            "                -Quando o Segundo Jogador for atirar e acertar um Navio, Aparecerá um [X] na coordenada digitada do mapa, já se ele errar, aparecerá um [O].")
        sleep(1)
        print("                -O jogo acaba quando o Jogador 2 derrubar todos os Navios.")
        sleep(1)
    sleep(2)
    print(" ")
    imprimirCampoTeste(campo)
    coordenadasFragataUm = input('Jogador 1, Informe as coordenadas da sua primeira Fragata :')
    if corrigirCoordenadaFragata(coordenadasFragataUm) is False:
        while corrigirCoordenadaFragata(coordenadasFragataUm) is False:
            coordenadasFragataUm = input('coordenadas invalidas. Tente novamente :')

    linhaFrUm = traduzirCoordenadasLinha(coordenadasFragataUm)
    colunaFrUm = traduzirCoordenadasColuna(coordenadasFragataUm)

    print(linhaFrUm + '\t' + colunaFrUm)

    if corrigirPosicaoFragata(campo, linhaFrUm, colunaFrUm) is False:
        while corrigirPosicaoFragata(campo, linhaFrUm, colunaFrUm) is False:
            coordenadasFragataUm = input('Ja há um barco nessas coordenadas. Digite a nova posicao do seu Navio :')

            if corrigirCoordenadaFragata(coordenadasFragataUm) is False:
                while corrigirCoordenadaFragata(coordenadasFragataUm) is False:
                    coordenadasFragataUm = input('coordenadas invalidas. Tente novamente :')
            else:
                linhaFrUm = traduzirCoordenadasLinha(coordenadasFragataUm)
                colunaFrUm = traduzirCoordenadasColuna(coordenadasFragataUm)

        linhaFrUm = traduzirCoordenadasLinha(coordenadasFragataUm)
        colunaFrUm = traduzirCoordenadasColuna(coordenadasFragataUm)

    print(linhaFrUm + '\t' + colunaFrUm)

    campo = posicionarFragata(campo, linhaFrUm, colunaFrUm)
    imprimirCampoTeste(campo)

    coordenadasFragataDois = input('Informe as coordenadas da fragata número Dois :')
    if corrigirCoordenadaFragata(coordenadasFragataDois) is False:
        while corrigirCoordenadaFragata(coordenadasFragataDois) is False:
            coordenadasFragataDois = input('coordenadas invalidas. Tente novamente :')

    linhaFrDois = traduzirCoordenadasLinha(coordenadasFragataDois)
    colunaFrDois = traduzirCoordenadasColuna(coordenadasFragataDois)

    print(linhaFrDois + '\t' + colunaFrDois)

    if corrigirPosicaoFragata(campo, linhaFrDois, colunaFrDois) is False:
        while corrigirPosicaoFragata(campo, linhaFrDois, colunaFrDois) is False:
            coordenadasFragataDois = input('Ja há um barco nessas coordenadas. Digite a nova posicao do seu Navio :')

            if corrigirCoordenadaFragata(coordenadasFragataDois) is False:
                while corrigirCoordenadaFragata(coordenadasFragataDois) is False:
                    coordenadasFragataDois = input('coordenadas inválidas. Tente novamente :')
            else:
                linhaFrDois = traduzirCoordenadasLinha(coordenadasFragataDois)
                colunaFrDois = traduzirCoordenadasColuna(coordenadasFragataDois)

        linhaFrDois = traduzirCoordenadasLinha(coordenadasFragataDois)
        colunaFrDois = traduzirCoordenadasColuna(coordenadasFragataDois)

    print(linhaFrDois + '\t' + colunaFrDois)

    campo = posicionarFragata(campo, linhaFrDois, colunaFrDois)
    imprimirCampoTeste(campo)

    coordenadasFragataTres = input('Informe as coordenadas da fragata número Três :')
    if corrigirCoordenadaFragata(coordenadasFragataTres) is False:
        while corrigirCoordenadaFragata(coordenadasFragataTres) is False:
            coordenadasFragataTres = input('coordenadas invalidas. Tente novamente :')

    linhaFrTres = traduzirCoordenadasLinha(coordenadasFragataTres)
    colunaFrTres = traduzirCoordenadasColuna(coordenadasFragataTres)

    print(linhaFrTres + '\t' + colunaFrTres)

    if corrigirPosicaoFragata(campo, linhaFrTres, colunaFrTres) is False:
        while corrigirPosicaoFragata(campo, linhaFrTres, colunaFrTres) is False:
            coordenadasFragataTres = input('Ja há um barco nessas coordenadas. Digite a nova posicao do seu Navio :')

            if corrigirCoordenadaFragata(coordenadasFragataTres) is False:
                while corrigirCoordenadaFragata(coordenadasFragataTres) is False:
                    coordenadasFragataTres = input('coordenadas inválidas. Tente novamente :')
            else:
                linhaFrTres = traduzirCoordenadasLinha(coordenadasFragataTres)
                colunaFrTres = traduzirCoordenadasColuna(coordenadasFragataTres)

        linhaFrTres = traduzirCoordenadasLinha(coordenadasFragataTres)
        colunaFrTres = traduzirCoordenadasColuna(coordenadasFragataTres)

    print(linhaFrTres + '\t' + colunaFrTres)

    campo = posicionarFragata(campo, linhaFrTres, colunaFrTres)
    imprimirCampoTeste(campo)

    coordenadasFragataQuatro = input('Informe as coordenadas da fragata número Quatro :')
    if corrigirCoordenadaFragata(coordenadasFragataQuatro) is False:
        while corrigirCoordenadaFragata(coordenadasFragataQuatro) is False:
            coordenadasFragataQuatro = input('coordenadas inválidas. Tente novamente :')

    linhaFrQuatro = traduzirCoordenadasLinha(coordenadasFragataQuatro)
    colunaFrQuatro = traduzirCoordenadasColuna(coordenadasFragataQuatro)

    print(linhaFrQuatro + '\t' + colunaFrQuatro)

    if corrigirPosicaoFragata(campo, linhaFrQuatro, colunaFrQuatro) is False:
        while corrigirPosicaoFragata(campo, linhaFrQuatro, colunaFrQuatro) is False:
            coordenadasFragataQuatro = input('Ja há um barco nessas coordenadas. Digite a nova posicao do seu Navio :')

            if corrigirCoordenadaFragata(coordenadasFragataQuatro) is False:
                while corrigirCoordenadaFragata(coordenadasFragataQuatro) is False:
                    coordenadasFragataQuatro = input('coordenadas invalidas. Tente novamente :')
            else:
                linhaFrQuatro = traduzirCoordenadasLinha(coordenadasFragataQuatro)
            colunaFrQuatro = traduzirCoordenadasColuna(coordenadasFragataQuatro)

        linhaFrQuatro = traduzirCoordenadasLinha(coordenadasFragataQuatro)
        colunaFrQuatro = traduzirCoordenadasColuna(coordenadasFragataQuatro)

    print(linhaFrQuatro + '\t' + colunaFrQuatro)

    campo = posicionarFragata(campo, linhaFrQuatro, colunaFrQuatro)
    imprimirCampoTeste(campo)

    coordenadasFragataCinco = input('Informe as coordenadas da fragata numero cinco :')
    if corrigirCoordenadaFragata(coordenadasFragataCinco) is False:
        while corrigirCoordenadaFragata(coordenadasFragataCinco) is False:
            coordenadasFragataCinco = input('coordenadas invalidas. Tente novamente :')

    linhaFrCinco = traduzirCoordenadasLinha(coordenadasFragataCinco)
    colunaFrCinco = traduzirCoordenadasColuna(coordenadasFragataCinco)

    print(linhaFrCinco + '\t' + colunaFrCinco)

    if corrigirPosicaoFragata(campo, linhaFrCinco, colunaFrCinco) is False:
        while corrigirPosicaoFragata(campo, linhaFrCinco, colunaFrCinco) is False:
            coordenadasFragataCinco = input('Ja ha um barco nessas coordenadas. Digite a nova posicao do seu Navio :')

            if corrigirCoordenadaFragata(coordenadasFragataCinco) is False:
                while corrigirCoordenadaFragata(coordenadasFragataCinco) is False:
                    coordenadasFragataCinco = input('coordenadas invalidas. Tente novamente :')
            else:
                linhaFrCinco = traduzirCoordenadasLinha(coordenadasFragataCinco)
            colunaFrCinco = traduzirCoordenadasColuna(coordenadasFragataCinco)

        linhaFrCinco = traduzirCoordenadasLinha(coordenadasFragataCinco)
        colunaFrCinco = traduzirCoordenadasColuna(coordenadasFragataCinco)

    print(linhaFrCinco + '\t' + colunaFrCinco)

    campo = posicionarFragata(campo, linhaFrCinco, colunaFrCinco)
    imprimirCampoTeste(campo)

    # posicionar cruzadores
    coordenadasCruzadorUm = input('Informe as coordenadas do seu primeiro Cruzador :')
    if corrigirCoordenadasCruzador(coordenadasCruzadorUm) is False:
        while corrigirCoordenadasCruzador(coordenadasCruzadorUm) is False:
            coordenadasCruzadorUm = input('coordenadas invalidas. Tente novamente :')

    linhaCrUm = traduzirCoordenadasLinha(coordenadasCruzadorUm)
    colunaCrUm = traduzirCoordenadasColuna(coordenadasCruzadorUm)

    print(linhaCrUm + '\t' + colunaCrUm)

    if corrigirPosicaoCruzador(campo, linhaCrUm, colunaCrUm) is False:
        while corrigirPosicaoCruzador(campo, linhaCrUm, colunaCrUm) is False:
            coordenadasCruzadorUm = input('Ja ha um barco nessas coordenadas. Digite a nova posicao do seu Navio :')

            if corrigirCoordenadasCruzador(coordenadasCruzadorUm) is False:
                while corrigirCoordenadasCruzador(coordenadasCruzadorUm) is False:
                    coordenadasCruzadorUm = input('coordenadas invalidas. Tente novamente :')
            else:
                linhaCrUm = traduzirCoordenadasLinha(coordenadasCruzadorUm)
                colunaCrUm = traduzirCoordenadasColuna(coordenadasCruzadorUm)

        linhaCrUm = traduzirCoordenadasLinha(coordenadasCruzadorUm)
        colunaCrUm = traduzirCoordenadasColuna(coordenadasCruzadorUm)

    print(linhaCrUm + '\t' + colunaCrUm)

    campo = posicionarCruzador(campo, linhaCrUm, colunaCrUm)
    imprimirCampoTeste(campo)

    coordenadasCruzadorDois = input('Informe as coordenadas do seu cruzador número Dois :')
    if corrigirCoordenadasCruzador(coordenadasCruzadorDois) is False:
        while corrigirCoordenadasCruzador(coordenadasCruzadorDois) is False:
            coordenadasCruzadorDois = input('coordenadas invalidas. Tente novamente :')

    linhaCrDois = traduzirCoordenadasLinha(coordenadasCruzadorDois)
    colunaCrDois = traduzirCoordenadasColuna(coordenadasCruzadorDois)

    print(linhaCrDois + '\t' + colunaCrDois)

    if corrigirPosicaoCruzador(campo, linhaCrDois, colunaCrDois) is False:
        while corrigirPosicaoCruzador(campo, linhaCrDois, colunaCrDois) is False:
            coordenadasCruzadorDois = input('Ja ha um barco nessas coordenadas. Digite a nova posicao do seu navio :')

            if corrigirCoordenadasCruzador(coordenadasCruzadorDois) is False:
                while corrigirCoordenadasCruzador(coordenadasCruzadorDois) is False:
                    coordenadasCruzadorDois = input('coordenadas invalidas. Tente novamente :')
            else:
                linhaCrDois = traduzirCoordenadasLinha(coordenadasCruzadorDois)
                colunaCrDois = traduzirCoordenadasColuna(coordenadasCruzadorDois)

        linhaCrDois = traduzirCoordenadasLinha(coordenadasCruzadorDois)
        colunaCrDois = traduzirCoordenadasColuna(coordenadasCruzadorDois)

    print(linhaCrDois + '\t' + colunaCrDois)

    campo = posicionarCruzador(campo, linhaCrDois, colunaCrDois)
    imprimirCampoTeste(campo)

    coordenadasCruzadorTres = input('Informe as coordenadas do seu cruzador número Três :')
    if corrigirCoordenadasCruzador(coordenadasCruzadorTres) is False:
        while corrigirCoordenadasCruzador(coordenadasCruzadorTres) is False:
            coordenadasCruzadorTres = input('coordenadas inválidas. Tente novamente :')

    linhaCrTres = traduzirCoordenadasLinha(coordenadasCruzadorTres)
    colunaCrTres = traduzirCoordenadasColuna(coordenadasCruzadorTres)

    print(linhaCrTres + '\t' + colunaCrTres)

    if corrigirPosicaoCruzador(campo, linhaCrTres, colunaCrTres) is False:
        while corrigirPosicaoCruzador(campo, linhaCrTres, colunaCrTres) is False:
            coordenadasCruzadorTres = input('Ja há um barco nessas coordenadas, digite a nova posicao do seu Navio :')

            if corrigirCoordenadasCruzador(coordenadasCruzadorTres) is False:
                while corrigirCoordenadasCruzador(coordenadasCruzadorTres) is False:
                    coordenadasCruzadorTres = input('coordenadas inválidas. Tente novamente :')
            else:
                linhaCrTres = traduzirCoordenadasLinha(coordenadasCruzadorTres)
                colunaCrTres = traduzirCoordenadasColuna(coordenadasCruzadorTres)

        linhaCrTres = traduzirCoordenadasLinha(coordenadasCruzadorTres)
        colunaCrTres = traduzirCoordenadasColuna(coordenadasCruzadorTres)

    print(linhaCrTres + '\t' + colunaCrTres)

    campo = posicionarCruzador(campo, linhaCrTres, colunaCrTres)
    imprimirCampoTeste(campo)

    coordenadasCruzadorQuatro = input('Informe as coordenadas do seu cruzador número Quatro :')
    if corrigirCoordenadasCruzador(coordenadasCruzadorQuatro) is False:
        while corrigirCoordenadasCruzador(coordenadasCruzadorQuatro) is False:
            coordenadasCruzadorQuatro = input('coordenadas inválidas. Tente novamente :')

    linhaCrQuatro = traduzirCoordenadasLinha(coordenadasCruzadorQuatro)
    colunaCrQuatro = traduzirCoordenadasColuna(coordenadasCruzadorQuatro)

    print(linhaCrQuatro + '\t' + colunaCrQuatro)

    if corrigirPosicaoCruzador(campo, linhaCrQuatro, colunaCrQuatro) is False:
        while corrigirPosicaoCruzador(campo, linhaCrQuatro, colunaCrQuatro) is False:
            coordenadasCruzadorQuatro = input('Ja há um barco nessas coordenadas, digite a nova posicao do seu Navio :')

            if corrigirCoordenadasCruzador(coordenadasCruzadorQuatro) is False:
                while corrigirCoordenadasCruzador(coordenadasCruzadorQuatro) is False:
                    coordenadasCruzadorQuatro = input('coordenadas inválidas. Tente novamente :')
            else:
                linhaCrQuatro = traduzirCoordenadasLinha(coordenadasCruzadorQuatro)
                colunaCrQuatro = traduzirCoordenadasColuna(coordenadasCruzadorQuatro)

        linhaCrQuatro = traduzirCoordenadasLinha(coordenadasCruzadorQuatro)
        colunaCrQuatro = traduzirCoordenadasColuna(coordenadasCruzadorQuatro)

    print(linhaCrQuatro + '\t' + colunaCrQuatro)

    campo = posicionarCruzador(campo, linhaCrQuatro, colunaCrQuatro)
    imprimirCampoTeste(campo)

    coordenadasPortaUm = input('Informe as coordenadas do seu primeiro Porta Aviões :')
    if corrigirCoordenadasPorta(coordenadasPortaUm) is False:
        while corrigirCoordenadasPorta(coordenadasPortaUm) is False:
            coordenadasPortaUm = input('coordenadas inválidas. Tente novamente :')

    linhaPoUm = traduzirCoordenadasLinha(coordenadasPortaUm)
    colunaPoUm = traduzirCoordenadasColuna(coordenadasPortaUm)

    print(linhaPoUm + '\t' + colunaPoUm)

    if corrigirPosicaoPorta(campo, linhaPoUm, colunaPoUm) is False:
        while corrigirPosicaoPorta(campo, linhaPoUm, colunaPoUm) is False:
            coordenadasPortaUm = input('Ja há um barco nessas coordenadas, digite a nova posicao do seu Navio :')

            if corrigirCoordenadasPorta(coordenadasPortaUm) is False:
                while corrigirCoordenadasPorta(coordenadasPortaUm) is False:
                    coordenadasPortaUm = input('coordenadas inválidas. Tente novamente :')
            else:
                linhaPoUm = traduzirCoordenadasLinha(coordenadasPortaUm)
                colunaPoUm = traduzirCoordenadasColuna(coordenadasPortaUm)

        linhaPoUm = traduzirCoordenadasLinha(coordenadasPortaUm)
        colunaPoUm = traduzirCoordenadasColuna(coordenadasPortaUm)

    print(linhaPoUm + '\t' + colunaPoUm)

    campo = posicionarPorta(campo, linhaPoUm, colunaPoUm)
    imprimirCampoTeste(campo)

    coordenadasPortaDois = input('Informe as coordenadas do seu Porta Aviões número Dois :')
    if corrigirCoordenadasPorta(coordenadasPortaDois) is False:
        while corrigirCoordenadasPorta(coordenadasPortaDois) is False:
            coordenadasPortaDois = input('coordenadas inválidas. Tente novamente :')

    linhaPoDois = traduzirCoordenadasLinha(coordenadasPortaDois)
    colunaPoDois = traduzirCoordenadasColuna(coordenadasPortaDois)

    print(linhaPoDois + '\t' + colunaPoDois)

    if corrigirPosicaoPorta(campo, linhaPoDois, colunaPoDois) is False:
        while corrigirPosicaoPorta(campo, linhaPoDois, colunaPoDois) is False:
            coordenadasPortaDois = input('Ja há um barco nessas coordenadas, digite a nova posicao do seu Navio :')

            if corrigirCoordenadasPorta(coordenadasPortaDois) is False:
                while corrigirCoordenadasPorta(coordenadasPortaDois) is False:
                    coordenadasPortaDois = input('coordenadas inválidas. Tente novamente :')
            else:
                linhaPoDois = traduzirCoordenadasLinha(coordenadasPortaDois)
                colunaPoDois = traduzirCoordenadasColuna(coordenadasPortaDois)

        linhaPoDois = traduzirCoordenadasLinha(coordenadasPortaDois)
        colunaPoDois = traduzirCoordenadasColuna(coordenadasPortaDois)

    print(linhaPoDois + '\t' + colunaPoDois)

    campo = posicionarPorta(campo, linhaPoDois, colunaPoDois)
    imprimirCampoTeste(campo)

    coordenadasPortaTres = input('Informe as coordenadas do seu Porta Aviões número Três :')
    if corrigirCoordenadasPorta(coordenadasPortaTres) is False:
        while corrigirCoordenadasPorta(coordenadasPortaTres) is False:
            coordenadasPortaTres = input('coordenadas inválidas. Tente novamente :')

    linhaPoTres = traduzirCoordenadasLinha(coordenadasPortaTres)
    colunaPoTres = traduzirCoordenadasColuna(coordenadasPortaTres)
    print(linhaPoTres + '\t' + colunaPoTres)

    if corrigirPosicaoPorta(campo, linhaPoTres, colunaPoTres) is False:
        while corrigirPosicaoPorta(campo, linhaPoTres, colunaPoTres) is False:
            coordenadasPortaTres = input('Ja há um barco nessas coordenadas, digite a nova posicao do seu Navio :')

            if corrigirCoordenadasPorta(coordenadasPortaTres) is False:
                while corrigirCoordenadasPorta(coordenadasPortaTres) is False:
                    coordenadasPortaTres = input('coordenadas inválidas. Tente novamente :')
            else:
                linhaPoTres = traduzirCoordenadasLinha(coordenadasPortaTres)
                colunaPoTres = traduzirCoordenadasColuna(coordenadasPortaTres)

        linhaPoTres = traduzirCoordenadasLinha(coordenadasPortaTres)
        colunaPoTres = traduzirCoordenadasColuna(coordenadasPortaTres)

    print(linhaPoTres + '\t' + colunaPoTres)

    campo = posicionarPorta(campo, linhaPoTres, colunaPoTres)
    # imprimirCampo(campo)

    print('\n' * 50)
    imprimirCampoTeste(campo)
    # fase de jogo
    pontuacao = 0
    while pontuacao < 220:

        tiro = input('Jogador 2, digite a posição onde deseja atirar :')
        if corrigirCoordenadaTiro(tiro) is False:
            while corrigirCoordenadaTiro(tiro) is False:
                tiro = input('coordenadas inválidas. Tente novamente :')

        linhaTiro = traduzirCoordenadasLinha(tiro)
        colunaTiro = traduzirCoordenadasColuna(tiro)
        print(linhaTiro + '\t' + colunaTiro)

        if corrigirPosicaoTiro(campo, linhaTiro, colunaTiro) is False:
            while corrigirPosicaoTiro(campo, linhaTiro, colunaTiro) is False:
                tiro = input('Voce já atirou nessa posicao. Tente novamente :')

                if corrigirCoordenadaTiro(tiro) is False:
                    while corrigirCoordenadaTiro(tiro) is False:
                        tiro = input('coordenadas inválidas. Tente novamente :')
                else:
                    linhaTiro = traduzirCoordenadasLinha(tiro)
                    colunaTiro = traduzirCoordenadasColuna(tiro)

            linhaTiro = traduzirCoordenadasLinha(tiro)
            colunaTiro = traduzirCoordenadasColuna(tiro)

        atirar(campo, linhaTiro, colunaTiro)
        campo = atirar(campo, linhaTiro, colunaTiro)

        pontuacaoFragata(campo, linhaFrUm, colunaFrUm, linhaFrDois, colunaFrDois, linhaFrTres, colunaFrTres,
                         linhaFrQuatro, colunaFrQuatro, linhaFrCinco, colunaFrCinco)
        pontuacaoCruzador(campo, linhaCrUm, colunaCrUm, linhaCrDois, colunaCrDois, linhaCrTres, colunaCrTres,
                          linhaCrQuatro, colunaCrQuatro)
        pontuacaoPorta(campo, linhaPoUm, colunaPoUm, linhaPoDois, colunaPoDois, linhaPoTres, colunaPoTres)

        pontuacaoF = pontuacaoFragata(campo, linhaFrUm, colunaFrUm, linhaFrDois, colunaFrDois, linhaFrTres,
                                      colunaFrTres, linhaFrQuatro, colunaFrQuatro, linhaFrCinco, colunaFrCinco)
        pontuacaoC = pontuacaoCruzador(campo, linhaCrUm, colunaCrUm, linhaCrDois, colunaCrDois, linhaCrTres,
                                       colunaCrTres, linhaCrQuatro, colunaCrQuatro)
        pontuacaoP = pontuacaoPorta(campo, linhaPoUm, colunaPoUm, linhaPoDois, colunaPoDois, linhaPoTres, colunaPoTres)

        pontuacao = calcularPontuacao(pontuacaoF, pontuacaoC, pontuacaoP)
        print('\n')
        imprimirCampoTeste(campo)
        print('\n'*3)
        #imprimirCampo(campo)
    print('Vitória !! a Frota Inimiga foi totalmente destruida')
    jogarnovamente = int(input("Deseja jogar novamente ? Digite 1 para sim ou 2 para sair :"))
    if jogarnovamente == 2:
        break


