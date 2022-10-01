''' JOGO ZOMBIE DICE
    REMI RODRIGUES NETO
    TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS '''

def quantidade():
    """
    Pede o número de jogadores

    :return: Retorna o número de jogadores
    """
    nj = 0
    while nj <= 1:
        nj = int(input("Por favor digite o número de jogadores: "))
        if nj <= 1:
            print("O número de jogadores deve ser no mínimo 2!")
    return nj

def lista():
    """
    Monta uma lista de jogadores e o placar com base no número inserido

    :return: Retorna a Lista de jogadores
    """
    placar = {}
    LJ = []
    for i in range(nj):
        nome = (input(f"Insira o nome do jogador {i + 1}: "))
        cerebro = 0
        placar[nome] = cerebro
        LJ.append(nome)
    return LJ, placar

import random
import sys

Verde = ("C", "P", "C", "T", "P", "C")
Amarelo = ("T", "P", "C", "T", "P", "C")
Vermelho = ("T", "P", "T", "C", "P", "T")

def sorteio():
    """
    Sorteia um dado e o remove do tubo

    :return: Retorna o dado sorteado
    """
    d1 = random.choice(tubo)
    tubo.remove(d1)
    if d1 <= 5:
        cor = "Verde"
        seq =  Verde
    elif d1>=6 and d1<=9:
        cor = "Amarelo"
        seq = Amarelo
    else:
        cor = "Vermelho"
        seq = Vermelho
    return cor, seq

def rodada():
    """
    Joga o dado

    :return: O lado que caiu o dado
    """
    dado = sorteio()
    print(dado[0])
    jogada = random.choice(dado[1])
    if jogada == "C":
        print("Você comeu um cérebro")
    elif jogada == "P":
        print("Sua vítima escapou!")
    else:
        print("Você levou um tiro")
    return jogada, dado

def checagem(passo):
    """
        Checa se foi rolado algum passo

    :param passo: dado a ser verificado
    :return: retorna passo se verdadeiro
    """
    if passo[0] == "P":
        dado = passo[1]
        print(dado[0])
        if dado == "Verde":
            cor = Verde
        elif dado == "Amarelo":
            cor = Amarelo
        else:
            cor = Vermelho
        jogada = random.choice(cor)
        if jogada == "C":
            print("Você comeu um cérebro")
        elif jogada == "P":
            print("Sua vítima escapou!")
        else:
            print("Você levou um tiro")
        return jogada, dado
    else:
        dado = sorteio()
        print(dado[0])
        if dado == "Verde":
            cor = Verde
        elif dado == "Amarelo":
            cor = Amarelo
        else:
            cor = Vermelho
        jogada = random.choice(cor)
        if jogada == "C":
            print("Você comeu um cérebro")
        elif jogada == "P":
            print("Sua vítima escapou!")
        else:
            print("Você levou um tiro")
        return jogada, dado

def soma(dado):
    """
    Verifica a face para contar a pontuação
    :param dado: Dado que foi lançado
    :return: Quantidade de cérebros e tiros
    """
    cer = 0
    tiro = 0
    if dado[0] == "C":
        cer += 1
    elif dado[0] == "T":
        tiro += 1
    else:
        pass
    return cer, tiro

def pontos():
    """
    Faz a soma da pontuação da jogada
    :return: Quantidade de cérebros e tiros total
    """
    cer = 0
    tiro = 0
    pcr = soma(d1)
    cer += pcr[0]
    tiro += pcr[1]
    pcr = soma(d2)
    cer += pcr[0]
    tiro += pcr[1]
    pcr = soma(d3)
    cer += pcr[0]
    tiro += pcr[1]
    return cer, tiro

nj = quantidade()
geral = lista()
LJ = geral[0]
placar = geral[1]
while nj == nj:
    print(f"O placar é de {placar}")
    for i in range(nj):
        tubo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        cer = 0
        tiro = 0
        print("Vez do jogador: ", LJ[i])
        seguir = True
        while seguir:
            if len(tubo) <= 2:
                tubo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            if len(tubo) == 13:
                print("Você tirou os dados:")
                d1 = rodada()
                d2 = rodada()
                d3 = rodada()
                pont = pontos()
                cer += pont[0]
                tiro += pont[1]
            else:
                print("Você tirou os dados:")
                d1 = checagem(d1)
                d2 = checagem(d2)
                d3 = checagem(d3)
                pont = pontos()
                cer += pont[0]
                tiro += pont[1]
            if tiro >= 3:
                print("Você tomou o terceiro tiro!!")
                seguir = False
            else:
                cont = input("Deseja jogar novamente? (s/n)")
            while seguir:
                if cont == "s":
                    break
                elif cont == "n":
                    placar[LJ[i]] += cer
                    if placar[LJ[i]] >= 13:
                        print(f"Parabéns, {LJ[i]} você ganhou o jogo")
                        print(f"O placar final foi {placar}")
                        sys.exit()
                    seguir = False
                else:
                    cont = input("Por favor digite s ou n para a decisão: ")
