def gerarMatriz(l, a):
    matriz = []
    for _ in range(0, a):
        matriz.append([0] * l)
    return matriz


def transformarEmMatriz(arquivo):
    l, a = [int(x) for x in arquivo[2].split()]
    dados = arquivo[4:len(arquivo)]
    matriz = gerarMatriz(l, a)
    for i in range(0, a):
        for j in range(0, l):
            matriz[i][j] = int(dados[j + (i * l)])
    return (matriz, l, a)


def formatoPPM(matriz, l, a):
    ppm = ['P2', str(l) + ' ' + str(a), '255']
    for i in range(0, a):
        for j in range(0, l):
            ppm += [str(matriz[i][j])]
    return ppm
