#n = total de peças.
#m = maximo de peças numa jogada.
# Se n é multiplo de m+1, o jogador começa, senão o computador.

def computador_escolhe_jogada(n,m):
    pecasRestantes = 0
    pecasRemovidas = 0
    if n == 1 or n == m or n < m:
        pecasRemovidas = n
        print(pecasRemovidas)
    else:
        pecasRemovidas = m
        pecasRestantes = n - m
        while pecasRestantes <= m and pecasRemovidas > 1:
            pecasRemovidas = pecasRemovidas - 1
            pecasRestantes = n - pecasRemovidas
            #print("pecasRemovidas:",pecasRemovidas, "-pecasRestantes",pecasRestantes)
    print("\nO Computador tirou",pecasRemovidas,"peças")
    return pecasRemovidas

def usuario_escolhe_jogada(n,m):
    pecasRemovidas = 0
    while pecasRemovidas <= 0:
        pecasRemovidas = int(input("\nQuantas peças você vai tirar?"))
        if pecasRemovidas > m:
            print("\nOops! Jogada inválida! Tente de novo.")
            pecasRemovidas = 0
        else:
            print("\nVocê tirou",pecasRemovidas,"peças.")
    return pecasRemovidas


def partida():
    n = 0
    while n <= 0:
        n = int(input("\nQuantas peças?"))
        m = int(input("Limite de peças por jogada?"))
        if n < m:
            print("\nLimite de peças por jogada inválida, tente de novo!")
            n = 0
        elif n <= 0:
            print("\nQuantidade de peças inválida, tente de novo!")
            n = 0
    totalPecas = n
    pecasRemovidas = 0
    # False -usuario
    # True - computador
    if (n % (m + 1) == 0):
        jogada = False
    else:
        jogada = True
            
    while n > 0:
        if not(jogada):
            if totalPecas == n:
                print("\nVoce começa!")
            pecasRemovidas = usuario_escolhe_jogada(n,m)
            n = n - pecasRemovidas
            if n == 0:
                print("Fim do jogo! Voce ganhou!")
            else:
                print("Agora restam",n, "peças no tabuleiro.")
                jogada = True
        else:
            if totalPecas == n:
                print("\nComputador começa!")
            pecasRemovidas = computador_escolhe_jogada(n,m)
            n = n - pecasRemovidas
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
            else:
                print("Agora restam",n, "peças no tabuleiro.")
                jogada = False


def campeonato():
    totalPartidas = 0
    placarUsuario = 0
    placarComputador = 0
    print("\nVoce escolheu um campeonato!\n")
    while totalPartidas != 3:
        totalPartidas = totalPartidas + 1
        if totalPartidas == 1:
            print("\n**** Rodada 1 ****\n")
            if partida():
                placarComputador = placarComputador + 1
            else:
                placarUsuario = placarUsuario + 1
        elif totalPartidas == 2:
            print("\n**** Rodada 2 ****\n")
            if partida():
                placarComputador = placarComputador + 1
            else:
                placarUsuario = placarUsuario + 1
        else:
            print("\n**** Rodada 3 ****\n")
            if partida():
                placarComputador = placarComputador + 1
            else:
                placarUsuario = placarUsuario + 1
            print("Placar: Você",placarUsuario,"X",placarComputador,"Computador")

def jogo():
    opcaoJogo = 0
    while opcaoJogo == 0:
        opcaoJogo = int(input("\nEscolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato:"))

        if opcaoJogo == 1:
            print("Partida isolada")
            partida()
        elif opcaoJogo == 2:
            campeonato()
        else:
            opcaoJogo = 0
            print("\nOpção inválida!")


print("\nBem-vindo ao jogo do NIM!")
jogo()

    
