# definição das jogadas
def menu_inicial():
 # inicio do jogo: menu de escolha da modalidade
    print('Bem-vindo ao jogo do NIM! Escolha:')
    resp = 0
    while resp != 1 and resp != 2:
        resp = int(input('''1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n _ '''))
    if resp == 1:
        print('Você escolheu jogar uma partida isolada!')
        print('-' * 15)
        partida()
    else:
        print('Você escolheu jogar um campeonato!')
        print('-' * 15)
        campeonato()

def usuario_escolhe_jogada(n, m):
    retirada_u = int(input('Quantas peças você vai tirar? _ '))
    while retirada_u > m or retirada_u <= 0:
        print('Oops! Jogada inválida! Tente de novo.')
        retirada_u = int(input('Quantas peças você vai tirar? _ '))
    print('Você tirou', retirada_u, 'peça(s)')
    return retirada_u


def computador_escolhe_jogada(n, m):
    # avalia se o n é maior que m. Se não for, então ja pode tirar todas as peças e ganhou o jogo.
    if m >= n:
        retirada_pc = n
        print('O computador tirou', retirada_pc, 'peças')
        print('Não resta nenhuma peça.\nO computador venceu!!!')
        print('-' * 15)
        return retirada_pc
    else:
    # se o número de peças n é maior que o limite para retirada m,
    # o computador precisa tirar peças de forma que o n restante
    # seja multiplo de (m + 1).
        retirada_pc = n % (m + 1)
        print('O computador retirou', retirada_pc, 'peças.')
        return retirada_pc

def partida():
    n = int(input('Quantidade de peças: _ '))
    m = int(input('Limite de peças por jogadas: _ '))
    if n % (m + 1) == 0:
        # jogador começa a partida
        print('Você começa!')
        retirada_u = usuario_escolhe_jogada(n, m)
        n -= retirada_u
        print('Restam', n, 'peças')
        print('-' * 15)
        while True:
            retirada_pc = computador_escolhe_jogada(n, m)
            n -= retirada_pc
            if n == 0:
                break
            else:
                print('Restam', n, 'peças')
                print('-' * 15)
                retirada_u = usuario_escolhe_jogada(n, m)
                n -= retirada_u
                print('Restam', n, 'peças')
                print('-' * 15)
    else:
        # computador começa a partida
        print('O computador começa!')
        retirada_pc = computador_escolhe_jogada(n, m)
        n -= retirada_pc
        if n != 0:
            print('Restam', n, 'peças')
            print('-' * 15)
            while True:
                retirada_u = usuario_escolhe_jogada(n, m)
                n -= retirada_u
                print('Restam', n, 'peças')
                print('-' * 15)
                retirada_pc = computador_escolhe_jogada(n, m)
                n -= retirada_pc
                if n == 0:
                    break
                else:
                    print('Restam', n, 'peças')
                    print('-' * 15)


def campeonato():
    print('*' * 15)
    placar = 0
    for c in range(3):
        print('-'*4, 'RODADA', c+1, '-'*4)
        partida()
        placar += 1
    print('*'*4, 'FINAL DO CAMPEONATO', '*'*4)
    print('Placar: Você 0 X', placar, 'Computador')



# programa principal
menu_inicial()