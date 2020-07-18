def caminhos_possiveis(inicio, fim, m):
    ''' Verifica todos os caminhos possíveis de 'inicio' a 'fim' em um grafo representado pela matriz adjacencia m.
    Os caminhos verificados não incluem os laços.

    :param inicio: vértice de origem dos caminhos a serem verificados (0 a n)
    :param fim: vértice de destino dos caminhos a serem verificados (0 a n)
    :param m: matriz adjacencia de um grafo
    :return: lista com todos os caminhos possíveis de 'inicio' a 'fim', excluíndo laços.
    Os elementos dessa lista representaram os vértices, em ordem, do caminho possível.
    '''

    y = len(m[inicio])  # número de colunas da matriz m
    caminhos = []  # lista final com todos os caminhos de 'inicio' a 'fim'
    temporaria = []  # lista que guarda os caminhos possíveis que saíram de 'início' mas ainda não chegaram a 'fim'
    temp = []  # lista temporária para inclusão dos índices
    zero = []  # lista temporária que inicia os caminhos

    # primeiro, preciso avaliar quem sai de 'inicio' e incluir esses valores em "zero"
    # para isso vou passar por todos os elementos de m[inicio] e ver quem é != 0 e guardar seu índice em "zero"
    for indice in range(y):
        if m[inicio][indice] != 0 and inicio != indice:
            zero.append(indice)
    # ok! ja sabemos as primeiras linhas que temos que observar.
    # vamos colocar então cada valor desses numa lista iniciando por "inicio" e incluir essa lista em 'temporária'
    for elemento in zero:
        temp.append(inicio)
        temp.append(elemento)
        if elemento != fim:
            temporaria.append(temp)
        else:
            caminhos.append(temp)
        temp = []
    # a lista 'temporária' ja tem o início de todos os caminhos.
    # a ideia agora é para o elemento '0' da lista temporaria ele ser atualizado e passado para o último
    # a cada elemento novo criado, será verificado se chegou ao fim do caminho. Os que chegaram, serão movidos para a lista 'caminhos'
    while not temporaria == []:
        i = temporaria[0][-1]
        for j in range(y):  # aqui eu verifico todos os elementos da linha.
            if m[i][j] != 0:  # aqui eu verifico e continuo só com os que seguem
                if j not in temporaria[0]:  # aqui eu verifico se o item ja nao está na lista temporaria[k] (para excluir laços)
                    temp = temporaria[0][:]
                    temp.append(j)
                    if temp[-1] != fim:
                        temporaria.append(temp)
                    else:
                        caminhos.append(temp)
        del temporaria[0]
    return caminhos


def menor_caminho(inicio, fim, m):
    ''' Indica o menor caminho (em quantidade de vértices) do 'inicio' a 'fim'

    :param inicio: vértice de origem (0 a n)
    :param fim: vértice de destino (0 a n)
    :param m: matriz adjacencia do grafo
    :return: lista com os vértices que compõe menor caminho
    '''

    caminhos = caminhos_possiveis(inicio, fim, m)
    menor = len(m) + 1
    menor_caminho = []
    for c in caminhos:
        if len(c) < menor:
            menor = len(c)
            menor_caminho = c
    return menor_caminho


def distancia_caminho(caminho, m):
    '''Retorna a distancia do caminho, conforme medida da matriz adjacencia

    :param caminho: caminho (vertices do caminho) para ser medida a distância
    :param m: matriz adjacencia do grafo
    :return: distancia
    '''

    if caminho not in caminhos_possiveis(caminho[0], caminho[-1], m):
        return 'Este não é um caminho da matriz informada'
    else:
        soma = 0
        for i in range(len(caminho)):
            if i != 0:
                soma += m[caminho[i - 1]][caminho[i]]
        return soma


# programa principal
# matriz adjacencia do grafo
m = [[0, 4, 2, 0, 0],
     [1, 0, 4, 6, 0],
     [2, 0, 4, 6, 8],
     [0, 9, 3, 0, 1],
     [0, 5, 0, 4, 0]]

inicio = 0
fim = 4
caminhos = caminhos_possiveis(inicio, fim, m)
print('caminhos possíveis:')
for i in caminhos:
    for j in i:
        print(j, end=' ')
        if j != fim:
            print('->', end = ' ')
    print()
print('-' * 20)


menor = menor_caminho(inicio, fim, m)
print('\nMenor caminho:')
for v in menor:
    print(v, end=' ')
    if v != fim:
        print('->', end=' ')
print()
print('-' * 20)
print()


menor_distancia = distancia_caminho(menor, m)
print('Distancia do menor caminho:')
print(menor_distancia)
print('-' * 20)
