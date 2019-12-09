import Matriz
import Arquivo


def lerMascara(caminho):
    mascArquivo = Arquivo.lerAquivo(caminho)
    m, n = [int(x) for x in mascArquivo[0].split()]
    dados = mascArquivo[1:len(mascArquivo)]
    mascara = Matriz.gerarMatriz(m, n)
    for i in range(0, m):
        for j in range(0, n):
            index = j + (i * m)
            mascara[i][j] = int(dados[index])
    return (mascara, m, n)


def aplicarMedia(matriz, lar, alt):
    mascara, m, n = lerMascara("Mascaras/media3x3.txt")
    peso = sum([sum(linha) for linha in mascara])

    a = int((m - 1) / 2)
    b = int((n - 1) / 2)
    largura = lar - (a * 2)
    altura = alt - (b * 2)
    aux = Matriz.gerarMatriz(largura, altura)
    for i in range(0, lar):
        for j in range(0, alt):
            if(i - a >= 0 and j - b >= 0 and i + a < lar and j + b < alt):
                for s in range(-a, a + 1):
                    for t in range(-b, b + 1):
                        aux[i - a][j - b] += mascara[a +
                                                     s][b + t] * matriz[i + s][j + t]
                aux[i - a][j - b] = round(aux[i - a][j - b] / peso)

    return (aux, largura, altura)


caminho = input('Digite o caminho do arquivo: ')
lista = Arquivo.lerAquivo(caminho)
matriz, largura, altura = Matriz.transformarEmMatriz(lista)

matriz, largura, altura = aplicarMedia(matriz, largura, altura)

ppm = Matriz.formatoPPM(matriz, largura, altura)
nome = input('Salvar como: ')
Arquivo.salvarArquivo(nome, ppm)
